"""
Intake-esgf attempt
"""

from intake_esgf.core.solr import SolrESGFIndex

searcher = SolrESGFIndex(index_node="esgf-node.ornl.gov", distrib=True)

search_res = searcher.search(source_id="CR-CMIP-1-0-0")
