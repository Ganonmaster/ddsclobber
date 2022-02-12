"""ddsclobber

Converts a DDS file, or folder with DDS files to TGA files, overwriting anything that already exists.

Written in python. Uses ImageMagick/Wand to do the conversion.

Usage:
  ddsclobber.py [FILE]

Options:
  -h --help     Show this screen.
  -v --version     Show version.

"""


from progressbar import ProgressBar, Bar, ETA, AdaptiveETA, FormatLabel, FormatCustomText
from docopt import docopt
from wand import image
import time
from pathlib import Path

def assert_dds(filename):
    """Ensure the file at a give path has the DDS magick-number
    header.  Throw an `AssertionError` if it does not match.
    """
    DDS_HEADER = [
        68, 68, 83
    ]
    with open(filename, 'rb') as fd:
        file_header = list(fd.read(3))
    assert file_header == DDS_HEADER



def process_file(filename):
    absolute_path = filename.resolve()
    destination_path = filename.with_suffix('.tga').resolve()
    with image.Image(filename=absolute_path) as img:
        img.compression = "no"
        img.save(filename=destination_path)

def run_file_conversion(file, errors):
    try:
        assert_dds(file)
        process_file(file)
    except AssertionError as e:
        errors.append(file)

    return errors


if __name__ == '__main__':
    arguments = docopt(__doc__, version='ddsclobber 0.1.0')

    # Get the list of files to process
    if arguments.get('FILE', False):
        input_path = arguments.get('FILE')
        print('Input path:', input_path)
        p = Path(input_path)
        errors = []

        # Processing a single file
        if p.is_file():
            print('Got a single file')
            errors = run_file_conversion(p, errors)
        else:
            # Processing a directory, show progress bar
            dds_contents = sorted(p.glob('**/*.dds'))
            print('Found ', len(dds_contents), '.DDS files')
            format_custom_text = FormatCustomText('Processing file: %(f)s', dict(f=''))
            
            widgets = [ format_custom_text, ' ', Bar(), ' ', ETA(), ' ', AdaptiveETA()]
            progress = ProgressBar(widgets=widgets)
            
            for file in progress(dds_contents):
                format_custom_text.update_mapping(f=file.resolve())
                errors = run_file_conversion(file, errors)

        print('Completed with', len(errors), 'error(s)')
        if errors:
            for error in errors:
                print('Invalid DDS file:', error)
