import os
import argparse
import openai

# setup the API key
home_dir = os.path.expanduser("~")
openai.api_key_path = os.path.join(home_dir, 'OPENAI_API_KEY')


def get_transcription(filename):
    with open(filename, 'rb') as fp:
        transcript = openai.Audio.translate("whisper-1", fp)
    return transcript['text']


def main(args):
    assert os.path.exists(args.input_audiofile)
    assert not os.path.exists(args.output)
    text = get_transcription(args.input_audiofile)

    with open(args.output, 'wt') as f:
        f.write(f'{text}\n')

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('input_audiofile', type=str)
   parser.add_argument('output', type=str)
   args = parser.parse_args()
   main(args)
