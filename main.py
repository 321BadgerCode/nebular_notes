from skyfield.api import load, Topos
from mido import Message, MidiFile, MidiTrack, MetaMessage
import datetime
import math

# Load ephemeris data
planets = load("./de421.bsp")
ts = load.timescale()
earth = planets["earth"]

# MIDI pitch bend conversion
def cents_to_pitchbend(cents):
	value = int((cents / 200.0) * 8192)
	return max(-8192, min(8191, value))

# Get planetary positions and derived parameters
def get_chart_data(date_str, time_str, lat, lon):
	dt = datetime.datetime.fromisoformat(f"{date_str}T{time_str}")
	t = ts.utc(dt.year, dt.month, dt.day, dt.hour, dt.minute)
	observer = earth + Topos(latitude_degrees=lat, longitude_degrees=lon)

	def ecliptic_deg(planet_name):
		obj = planets[planet_name].at(t).observe(observer).ecliptic_latlon()
		return obj[1].degrees % 360

	mars_lon = ecliptic_deg("mars")
	moon_lon = ecliptic_deg("moon")
	mercury_lon = ecliptic_deg("mercury")

	angle = abs(mars_lon - moon_lon) % 360
	if angle > 180:
		angle = 360 - angle

	return {
		"mars_lon": mars_lon,
		"moon_lon": moon_lon,
		"mercury_lon": mercury_lon,
		"angle_deg": angle
	}

# Generate MIDI
def generate_midi(filename, chart_data):
	midi = MidiFile()
	track = MidiTrack()
	midi.tracks.append(track)

	# Parameter mappings
	tempo_bpm = int(60 + (chart_data["mars_lon"] / 360.0) * 180)
	pitch_cents = ((chart_data["angle_deg"] / 180.0) * 200.0) - 100.0
	pitch_bend = cents_to_pitchbend(pitch_cents)
	velocity = int(40 + (chart_data["moon_lon"] / 360.0) * 87)
	note_duration = int(240 + (chart_data["mercury_lon"] / 360.0) * 480)

	# Set tempo
	tempo_meta = int(60_000_000 / tempo_bpm)
	track.append(MetaMessage("set_tempo", tempo=tempo_meta))

	# Add 8-note melody with pitch bend
	scale = [60, 62, 64, 65, 67, 69, 71, 72] # C major as base
	for i, note in enumerate(scale):
		# Apply pitch bend before note
		track.append(Message("pitchwheel", pitch=pitch_bend, time=0))
		track.append(Message("note_on", note=note, velocity=velocity, time=0))
		track.append(Message("note_off", note=note, velocity=velocity, time=note_duration))

	# Reset pitch bend
	track.append(Message("pitchwheel", pitch=0, time=0))
	midi.save(filename)
	print(f"[+] MIDI saved to: {filename}")
	print(f"	Tempo: {tempo_bpm} BPM")
	print(f"	Pitch bend: {pitch_cents:.2f} cents ({pitch_bend})")
	print(f"	Velocity: {velocity}")
	print(f"	Note duration: {note_duration} ticks")

# Example usage
if __name__ == "__main__":
	# London in 1995
	date = "1995-06-15"
	time = "12:00:00"
	lat = 51.5074
	lon = -0.1278
	chart = get_chart_data(date, time, lat, lon)
	generate_midi("astro_microtonal_output_london.mid", chart)

	# Germany in 1945
	date = "1945-05-08"
	time = "07:48:12"
	lat = 51.1657
	lon = 10.4515
	chart = get_chart_data(date, time, lat, lon)
	generate_midi("astro_microtonal_output_germany.mid", chart)

	# Tokyo in 2020
	date = "2020-12-31"
	time = "23:59:59"
	lat = 35.682839
	lon = 139.759455
	chart = get_chart_data(date, time, lat, lon)
	generate_midi("astro_microtonal_output_tokyo.mid", chart)