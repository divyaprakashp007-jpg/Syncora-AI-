
def test_sample_data_has_matching_resource_types():
    needs = [
        {"type": "need", "resource": "Mentorship"},
        {"type": "need", "resource": "Computer"},
    ]

    offers = [
        {"type": "offer", "resource": "Mentorship"},
        {"type": "offer", "resource": "Computer"},
    ]

    for need in needs:
        assert any(
            offer["type"] == "offer"
            and offer["resource"] == need["resource"]
            for offer in offers
        )


def test_no_match_for_unavailable_resource():
    needs = [{"type": "need", "resource": "Medical Equipment"}]
    offers = [{"type": "offer", "resource": "Mentorship"}]

    matches = [
        offer for offer in offers
        if offer["resource"] == needs[0]["resource"]
    ]

    assert matches == []
