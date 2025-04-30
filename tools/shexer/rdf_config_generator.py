import os
import argparse
import sys
from shexer.shaper import Shaper
from shexer.consts import TURTLE, MIXED_INSTANCES, ALL_EXAMPLES, GZ, XZ, RDF_XML, TURTLE_ITER

def run(base_input_dir,
        out_path,
        namespaces):

   in_files = [os.path.join(dp, f) for dp, dn, filenames in
                os.walk(base_input_dir) for f in filenames
                if os.path.splitext(f)[1] == '.gz']
   print("Input files: ", in_files)
   shaper = Shaper(graph_list_of_files_input=in_files,
                   input_format=TURTLE,
                   all_classes_mode=True,
                   namespaces_dict=namespaces,
                   disable_exact_cardinality=True,
                   detect_minimal_iri=True,
                   compression_mode="gz",
                   instances_report_mode=MIXED_INSTANCES,
                   examples_mode=ALL_EXAMPLES)

   rdfconfig_dir =  "./rdfconfig"

   shaper.shex_graph(
       output_file=out_path,
       rdfconfig_directory=rdfconfig_dir,
       verbose=True,
       acceptance_threshold=0.05
   )

   print("Done!")

if __name__ == "__main__":
    ############### CONFIGURATION ###############

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Specify the input directory')
    parser.add_argument('-o', '--output', help='Specify the output file')
    args = parser.parse_args()
    if args.input:
       base_input_dir = args.input
    else:
       print('Specify the input directory.', file=sys.stderr)
       sys.exit(-1)
    if args.output:
       out_path = args.output
    else:
       out_path = "__STD_OUT__"

    # namespace-prefix pair to be used in the results
    namespaces_dict = {"http://purl.org/dc/terms/": "dc",
                       "http://rdfs.org/ns/void#": "void",
                       "http://www.w3.org/2001/XMLSchema#": "xsd",
                       "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf",
                       "http://purl.org/pav/": "pav",
                       "http://www.w3.org/ns/dcat#": "dcat",
                       "http://xmlns.com/foaf/0.1/": "foaf",
                       "http://www.w3.org/2002/07/owl#": "owl",
                       "http://www.w3.org/2000/01/rdf-schema#": "rdfs",
                       "http://www.w3.org/2004/02/skos/core#": "skos",
                       }
    ############### EXECUTION ###############

    run(base_input_dir=base_input_dir,
        out_path=out_path,
        namespaces=namespaces_dict)
