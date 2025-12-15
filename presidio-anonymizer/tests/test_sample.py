from presidio_anonymizer.sample import sample_run_anonymizer


def test_sample_run_anonymizer_anonymizes_person_name():
    # Arrange
    text = "My name is Bond."
    start = 11
    end = 15

    # Act
    result = sample_run_anonymizer(
        text=text,
        start=start,
        end=end,
    )

    # Assert: output structure
    assert result is not None
    assert hasattr(result, "text")
    assert hasattr(result, "items")

    # Assert: anonymized text
    assert result.text == "My name is BIP."

    # Assert: anonymization metadata
    assert len(result.items) == 1

    item = result.items[0]

    # OperatorResult uses attributes, not dict keys
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
    assert item.start == 11
    assert item.end == 14
