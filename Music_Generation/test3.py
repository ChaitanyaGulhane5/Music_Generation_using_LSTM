import pretty_midi
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def extract_pitch_and_frequency(midi_file_path, num_notes=20):
    pitch_data = []
    frequency_data = []

    # Load the MIDI file
    midi_data = pretty_midi.PrettyMIDI(midi_file_path)

    # Counter to track the number of sampled notes
    note_count = 0

    # Iterate through all instruments in the MIDI file
    for instrument in midi_data.instruments:
        for note in instrument.notes:
            # Extract the pitch (note number) and frequency
            pitch = note.pitch
            frequency = pretty_midi.note_number_to_hz(pitch)

            # Append the data to the lists
            pitch_data.append(pitch)
            frequency_data.append(frequency)

            # Increment the note count
            note_count += 1

            # Break the loop if the desired number of notes is sampled
            if note_count == num_notes:
                break

        # Break the loop if the desired number of notes is sampled
        if note_count == num_notes:
            break

    return pitch_data, frequency_data

def smooth_data(data, window_size=3):
    df = pd.DataFrame(data)
    smoothed_data = df.rolling(window=window_size).mean().iloc[window_size-1:].values.flatten()
    return smoothed_data

# Example usage
midi_file_path = '/home/deepakachu/Desktop/DMS/project_final/generated_music/5_800_0.mid-a.mid'
num_notes_to_sample = 20
pitch_data, frequency_data = extract_pitch_and_frequency(midi_file_path, num_notes_to_sample)

# Smoothing the data
window_size = 3  # Adjust the window size as needed
smoothed_pitch_data = smooth_data(pitch_data, window_size)
smoothed_frequency_data = smooth_data(frequency_data, window_size)

# Plotting with an elongated x-axis
plt.figure(figsize=(15, 5))  # Set the width and height of the plot
plt.plot(smoothed_pitch_data, 'o-', label='Smoothed Pitch (Note Number)')
plt.plot(smoothed_frequency_data, 's-', label='Smoothed Frequency (Hz)')
plt.xlabel('Note Index')
plt.ylabel('Value')
plt.title('Smoothed Pitch and Frequency of MIDI Notes')
plt.legend()
plt.show()
