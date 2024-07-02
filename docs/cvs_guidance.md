# Controlled vocabularies guidance

This doc is a placeholder for capturing notes about the rules
which apply to our controlled vocabularies (CVs).
It will be superseded by code which actually implements these rules
(and code is much more precise than words, hence these docs will
be replaced by docs documenting the code instead).
Lots of thinking about this has been done already, and will be used to build
out the code which implements the rules, e.g.:

- https://docs.google.com/document/d/1h0r8RZr_f3-8egBMMh7aqLwy3snpD6_MrDz1q8n5XUk/edit
- https://docs.google.com/document/d/1oLK4mWW6TX2YPrhGoLdMLcrK7vX1flU3BjiheTb2Hwk/edit

## Source ID

The source ID is the key way of registering a contribution to ESGF.
The source ID then also defines other common metadata.
Any field can be placed in source ID.
This provides flexibility for data providers to add extra information specific to their use case.
Some fields you may consider including are references, comment
Having said this, the following fields are compulsory in each source ID submission:

- activity_id
    - this must match an activity ID in `input4MIPs_activity_id.json`
- contact
    - a valid email is expected here
- further_info_url
    - a valid URL or the placeholder, "TBD", is expected here
- institution
    - this can be any string, which allows you to put a longer name for your institution
- institution_id
    - this must match an institution in `input4MIPs_institution_id.json`
      (although is likely going to be replaced soon by having to match an institution ID
      in a more general repo I can't find right now)
- license
    - the license which applies to your data
    - it must match the expression given in `input4MIPs_license.json`
- mip_era
    - this must match a value in `input4MIPs_activity_id.json`
- source_version
    - the version of your data
- version
    - the version of your data
    - [TODO: check how/if this differs from source_version]
