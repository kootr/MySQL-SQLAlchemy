# MySQL-SQLAlchemy

Experiment for SQLAlchemy


# Result

```bash
❯ python sql.py
get_by_JourneySchema {'journey_id': '9fd3fa6c-01ca-485a-a73f-edc436bbddeb', 'client_id': 44, 'number_of_users': 5}
get_by_JourneyMapper {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x102ad25c0>, 'id': 1, 'journey_id': '9fd3fa6c-01ca-485a-a73f-edc436bbddeb', 'client_id': 44}

```

# MySQL Database

```bash
mysql> select * from journey;
+----+--------------------------------------+-----------+
| id | journey_id                           | client_id |
+----+--------------------------------------+-----------+
|  1 | 9fd3fa6c-01ca-485a-a73f-edc436bbddeb |        44 |
+----+--------------------------------------+-----------+
1 row in set (0.00 sec)

mysql>
```
