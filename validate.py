import logging
import jsonschema

logger = logging.getLogger()


def is_line_valid(line_data: dict) -> bool:
    schema = {
        "type": "object",
        "properties": {
            "DataOwnerCode": {"type": "string"},
            "LinePlanningNumber": {"type": "string"},
            "LineDirection": {"type": "integer"},
            "LinePublicNumber": {"type": "string"},
            "LineName": {"type": "string"},
            "DestinationName50": {"type": "string"},
            "DestinationCode": {"type": "string"},
            "LineWheelchairAccessible": {"type": "string", "enum": ["ACCESSIBLE", "NOTACCESSIBLE", "UNKNOWN"]},
            "TransportType": {"type": "string", "enum": ["BUS", "TRAIN", "METRO", "BOAT", "TRAM"]},
        },
        "required": ["DataOwnerCode", "LinePlanningNumber", "LineDirection"]
    }

    try:
        jsonschema.validate(instance=line_data, schema=schema)
    except jsonschema.ValidationError as e:
        logger.info(f"Error {e} on line {line_data}")
        return False

    return True


def validate_data(ovapi_data: dict) -> list[dict]:
    return [line_data for line_data in ovapi_data.values() if is_line_valid(line_data)]
