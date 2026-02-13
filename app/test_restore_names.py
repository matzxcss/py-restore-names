import pytest

import app.restore_names as main


@pytest.mark.parametrize(
    "users, expected_first_name, full_name_expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            "Jack",
            "Jack Holy",
        ),
        (
            [
                {
                    "last_name": "Days",
                    "full_name": "Cleber Days",
                }
            ],
            "Cleber",
            "Cleber Days",
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            "Mike",
            "Mike Adams",
        ),
        (
            [
                {
                    "first_name": "Alice",
                    "last_name": "Cooper",
                    "full_name": "Alice Cooper",
                }
            ],
            "Alice",
            "Alice Cooper",
        ),
    ],
)
class TestRestoreName:
    def test_restore_name(
        self,
        users: list[dict],
        expected_first_name: str,
        full_name_expected: str,
    ) -> None:
        for user in users:
            main.restore_names([user])
            assert user["first_name"] == expected_first_name
            assert user["full_name"] == full_name_expected

    def test_first_name(self, users: list[dict]) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
            {
                "first_name": "Alice",
                "last_name": "Cooper",
                "full_name": "Alice Cooper",
            },
        ]
        main.restore_names(users)
        assert users[0]["first_name"] == "Jack"
        assert users[1]["first_name"] == "Mike"
        assert users[2]["first_name"] == "Alice"
