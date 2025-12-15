from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(
    text: str,
    start: int,
    end: int,
    entity_type: str = "PERSON",
    score: float = 0.8,
    new_value: str = "BIP",
):
    # Initialize the engine
    engine = AnonymizerEngine()

    # Invoke the anonymize function with the text,
    # analyzer results (potentially coming from presidio-analyzer) and
    # Operators to get the anonymization output:
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(
                entity_type=entity_type,
                start=start,
                end=end,
                score=score,
            )
        ],
        operators={
            entity_type: OperatorConfig("replace", {"new_value": new_value})
        },
    )

    print(result)

    # input should be:
    # text: My name is Bond.
    # start: 11
    # end: 15
    #
    # output should be:
    # text: My name is BIP.
    # items:
    # [
    #     {'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}
    # ]

    # Return result so tests can assert on it
    return result


if __name__ == "__main__":
    # The returned result should be saved to a variable
    anonymized_result = sample_run_anonymizer(
        text="My name is Bond.",
        start=11,
        end=15,
    )
