'''
Script honek nemo environment-a erabiltzen du.
Nemo instalatzeko jarraitu github-eko pausoak, gatai notatan adierazi den modura
'''


import os
import sys
import re
import nemo.collections.asr as nemo_asr

def transcribe_audio_files(start_path):
    # Load the ASR model
    model_name = "stt_eu_conformer_transducer_large.nemo"
    model = nemo_asr.models.ASRModel.restore_from(model_name)

    for root, dirs, files in os.walk(start_path):
        for file in files:
            # Check if the file matches the required pattern
            if re.match(r'.*_low\d{3}\.wav$', file):
                full_path = os.path.join(root, file)
                print(f"Transcribing file: {full_path}")

                # Perform transcription
                transcript = model.transcribe([full_path], channel_selector=0)

                # Save the transcript
                transcript_file = full_path.rsplit('.', 1)[0] + '.txt'  # Replace .wav with .txt
                with open(transcript_file, 'w') as f:
                    f.write(transcript[0][0])
                print(f"Transcription saved to: {transcript_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.isdir(path):
        print(f"The path {path} is not a directory or does not exist.")
        sys.exit(1)

    transcribe_audio_files(path)



'''
conda activate nemo


run with /home/ilopez077/scratch/Gatai/Data/Album ilustratuen grabazioak (elkarrizketa sakonak)/WAV_DOWNSAMPLED params

python transcribe.py /home/ilopez077/scratch/Gatai/Data/Album\ ilustratuen\ grabazioak\ \(elkarrizketa\ sakonak\)/

'''
