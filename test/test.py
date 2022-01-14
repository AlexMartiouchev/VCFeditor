import json
import os
from VCFeditor.settings import BASE_DIR, MEDIA_ROOT

f = open(os.path.join(BASE_DIR, MEDIA_ROOT, "NA128_API_10_mini.vcf"))
f = f.read()
pre_list = f.split("\n")
meta_list = []
header_list = []
variant_list = []
variant_tmp_list = []
variant_dict = {}
variants_final = []


if pre_list[-1] == "":  # removes interfering blank last line
    pre_list.pop()


for line in pre_list:
    line = line.split("\t")
    if line[0][0] == "#" and line[0][1] == "#":
        meta_list.append(line)
    elif line[0][0] == "#":
        header_list = line[:5]
        header_list[0] = header_list[0][1:]
    else:
        variant_tmp_list = line
        variant_list = variant_tmp_list[:5]
        n = 0
        for item in variant_list:
            variant_dict.update({header_list[n]: variant_list[n]})
            n += 1
        variants_final.append(variant_dict)

variants_json = json.dumps(variants_final)
print(variants_json)
print(len(variants_final))
