def common_format_list_tags(result_tags, insert_tags, tags_index=10):
    if insert_tags is not None and len(insert_tags) > 0:
        insert_tag_list = insert_tags[0:tags_index]
        for tag in insert_tag_list:
            if isinstance(tag, str):
                if tag and tag.strip() != "":
                    result_tags.append(tag)


def common_format_string_tags(result_tags, data, key):
    if data.get(key) is not None and data.get(key) != "":
        result_tags.append(data.get(key))
    return result_tags

"""

# 政策通 政策标签
def format_policy_tags(policy):
    shangqi_tags = policy.get("tags",{})

    result_tags = {
        "support_object":policy.get("support_object", []),
        "support_way":policy.get("support_way", [])
    }

    common_format_list_tags(tags, )

    common_format_list_tags(tags, policy.get("support_behavior", []))
    common_format_string_tags(tags, policy, "is_declare")
    if shangqi_tags:
        industry_tags = [data["tag_name"] for data in shangqi_tags.get("industry_tag",[])]
        certification_tags = shangqi_tags.get("certification_tag",[])
        common_format_list_tags(tags, industry_tags)
        common_format_list_tags(tags, certification_tags)

    tags_list = [{
        "type": "other",
        "tabs": tags
    }]
    if policy.get("tags"):
        tags = policy["tags"]
        tags_list.append({
            "type": "产业类型",
            "tabs": [data["tag_name"] for data in tags.get("industry_tag", [])]
        })
    return tags_list


"""