"""
Endpoint and key management for neocasa.
I think It's best to setup the keys and endpoints once, and then use everywhere, instead of setting it up in every file, or every where it is needed.
so, if the need to change arise, then changes will be made easier.
please note: this module will assume you have the following :
* neospeechkey and neospeechendpoint for the speech services,
* neovisionkey and neovisionendpoint for the vision services used in this project.
If you have something different, edit this file, or change your enviroment variable.
Or better still, change the method of authentication It's all up to you! But I'll like to here it, if I will adapt it too.
"""
import os
import re

# key and endpoint for azure speech api:
speechkey, speechendpoint = os.environ["neospeechkey"], os.environ["neospeechendpoint"]
# keys and endpoint for the azure vision api:
visionkey, visionendpoint = os.environ["neovisionkey"], os.environ["neovisionendpoint"]
# first things first:
# don't waste your time sending what won't work.
# for example: sending an empty key/endpoint, or even what doesn't look like it.
# The key is a 32-character HEX number (no dashes), found in the Azure portal

# Microsoft has provided a code in their sample repo: https://github.com/Azure-Samples/azure-ai-vision-sdk/
# let's use some things in this repo with little modifications.
def is_valid_endpoint(endpoint):
    """
    Validates the format of the Computer Vision Endpoint URL.
    Returns True if the endpoint is valid, False otherwise.
    """
    if endpoint is None or len(endpoint) == 0:
        print(" Error: Missing computer vision endpoint.")
        print()
        return False

    if re.search(r"^https://\S+\.cognitiveservices\.azure\.com/?$", endpoint):
        return True
    else:
        print(" Error: Invalid value for computer vision endpoint: {}".format(endpoint))
        print(" It should be in the form:")
        print(" https://<your-computer-vision-resource-name>.cognitiveservices.azure.com")
        print()
        return False

#is_valid_key(visionkey)
#is_valid_endpoint(visionendpoint)