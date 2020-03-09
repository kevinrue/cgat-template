#!/usr/bin/env python3

# Arguments
# name: name of the new pipeline

# Make a copy of the pipeline script under the new name
# cp -r pipeline_template.py pipeline_<new_name>.py

# Make a copy of the pipeline folder under the new name
# cp -r pipeline_template pipeline_<new_name>


# Substitute occurences of "template" following "pipeline" by the new name
## pipeline.yml
### "Pipeline template" -> "Pipeline <new name>"
## pipeline_template.py
### "Pipeline template" -> "Pipeline <new name>"
### "pipeline_template.py" -> "pipeline_<new name>.py"

def main():
    """Docstring.
    """

    # setup command line parser
    parser = ArgumentParser(description=__doc__)

    parser.add_argument("--version", action='version', version="1.0")

    parser.add_argument("-f", "--bam-file", "--filename", dest="filename", type=str,
                        help="bamfile")

    parser.add_argument("-a", "--aligner", dest="aligner", type=str,
                        help="bamfile", default="bwa")

    parser.add_argument("-r", "--output-report", type=str, dest="report",
                        help="bamfile", default="")

    parser.add_argument("-o", "--output-filename-bam", "--outfile", dest="outfile", type=str,
                        help="bamfile", default="")

    # add common options (-h/--help, ...) and parse command line
    (args) = E.start(parser, argv=argv, add_output_options=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv))