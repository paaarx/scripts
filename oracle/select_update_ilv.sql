/*
    Author: https://github.com/paaarx
    Description: Select update with In Line View (ILV), it allows joins too.
    Tested: Oracle 11g R2
*/
UPDATE
    (SELECT
        id,
        field_1,
        field_2
    FROM
        a_table
    WHERE
        field_3 = 'condition'
    ) ilv
SET
    ilv.field_1 = ilv.field_2
WHERE
    ilv.id = ilv.id;
