from processes.validate import validate_data


def test_validate_data():
    expected = [
        {
            "DataOwnerCode": "A",
            "LineWheelchairAccessible": "ACCESSIBLE",
            "TransportType": "TRAM",
            "DestinationName50": "Somewhere",
            "DestinationCode": "1",
            "LinePublicNumber": "A",
            "LinePlanningNumber": "1",
            "LineName": "A",
            "LineDirection": 1
        },
    ]
    ovapi_data = {
        "A": {
            "DataOwnerCode": "A",
            "LineWheelchairAccessible": "ACCESSIBLE",
            "TransportType": "TRAM",
            "DestinationName50": "Somewhere",
            "DestinationCode": "1",
            "LinePublicNumber": "A",
            "LinePlanningNumber": "1",
            "LineName": "A",
            "LineDirection": 1
        },
        "B": {
            "DataOwnerCode": "A",
            "LineWheelchairAccessible": "ACCESSIBLE",
            "TransportType": "TRAM",
            "DestinationName50": "Somewhere",
            "DestinationCode": "1",
            "LinePublicNumber": "A",
            "LinePlanningNumber": "1",
            "LineName": "A",
            "LineDirection": "1"
        },
        "C": {
            "LineWheelchairAccessible": "ACCESSIBLE",
            "TransportType": "TRAM",
            "DestinationName50": "Somewhere",
            "DestinationCode": "1",
            "LinePublicNumber": "A",
            "LinePlanningNumber": "1",
            "LineName": "A",
            "LineDirection": "1"
        },
        "D": {
            "DataOwnerCode": "A",
            "LineWheelchairAccessible": "ACCESSIBLE",
            "TransportType": "PLANE",
            "DestinationName50": "Somewhere",
            "DestinationCode": "1",
            "LinePublicNumber": "A",
            "LinePlanningNumber": "1",
            "LineName": "A",
            "LineDirection": "1"
        },
    }
    assert validate_data(ovapi_data) == expected


if __name__ == '__main__':
    test_validate_data()
