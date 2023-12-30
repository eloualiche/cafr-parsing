import argparse
from miner import process_pdf  # Importing the function from miner.py

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a PDF file.')
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    args = parser.parse_args()

    process_pdf(args.pdf_path)


# python cli.py data/ID_cafr2010.pdf
# ## For now you can test this code by uncommenting and picking a file path
# process_pdf("data/ID_cafr2010.pdf")
# process_pdf("data/ID_cafr2011.pdf")
# process_pdf("data/ID_cafr2012.pdf")
# process_pdf("data/ID_cafr2013.pdf")
# process_pdf("data/ID_cafr2014.pdf")
# process_pdf("data/NY_cafr2010.pdf")
# process_pdf("data/NY_cafr2011.pdf")
# process_pdf("data/NY_cafr2012.pdf")
# process_pdf("data/NY_cafr2013.pdf")
# process_pdf("data/NY_cafr2014.pdf")