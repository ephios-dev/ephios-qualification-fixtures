# ephios-qualification-fixtures
Contains fixtures of commonly used qualifications for ephios.

## TODO

When importing to ephios, we need to

* created needed qualifications
* check that newly added qualifications are included in the correct existing ones
* check that newly added qualifications include the correct existing ones
* check that removing a qualification does not break a chain of inclusion
* check that adding a subset of a fixture's qualifications keeps all inclusions

To achieve this, we might normalize the fixtures in a way 
that every qualifications includes *every* qualification from transitivity.