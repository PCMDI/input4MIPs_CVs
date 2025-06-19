import pandas as pd
import requests

# From what I can tell, you can only get 10 000 results at a time
# so have to group searches somehow
# Hard-coding obviously not ideal,
# but pattern is pretty easy to spot
# so it shouldn't be hard to group by a different facet
res_file = "input4mips-cmip7.csv"
r_source_ids = requests.get(
    "https://esgf-node.ornl.gov/esgf-1-5-bridge?replica=false&limit=0&type=File&activity_id=input4MIPs&mip_era=CMIP7&facets=source_id"
)
r_source_ids_json = r_source_ids.json()


source_ids_n_results_d = {
    source_id: int(n_results)
    for source_id, n_results in zip(
        r_source_ids_json["facet_counts"]["facet_fields"]["source_id"][::2],
        r_source_ids_json["facet_counts"]["facet_fields"]["source_id"][1::2],
    )
}

results_df_l = []
for source_id, n_results in source_ids_n_results_d.items():
    if n_results > 10_000:
        msg = f"The API is limited to returning 10 000 results, but {source_id} has {n_results}"
        raise AssertionError(msg)

    url_to_hit = f"https://esgf-node.ornl.gov/esgf-1-5-bridge?replica=false&limit={n_results}&type=File&activity_id=input4MIPs&source_id={source_id}"
    print(f"Fetching {source_id} from\n{url_to_hit}")
    r_source_id = requests.get(url_to_hit)
    r_source_id_json = r_source_id.json()

    results_df_l.append(pd.DataFrame(r_source_id_json["response"]["docs"]))
    print()

results_df = pd.concat(results_df_l)
results_df.to_csv(res_file)
print(results_df)
