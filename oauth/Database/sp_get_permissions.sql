SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
DELIMITER $$
DROP PROCEDURE if exists sp_get_permissions$$
CREATE DEFINER=`root`@`%` PROCEDURE `sp_get_permissions`(IN `app_id` VARCHAR(256), IN `role_id` INT)
    NO SQL
SELECT
        JSON_OBJECT(
            "id",
            role.id,
            "name",
            role.name,
            "resources",
            JSON_ARRAYAGG(resources.resources_data)
        )
    FROM
        `role`,
        (
        SELECT
            role_permission.role_id AS `role_id`,
            JSON_OBJECT(
                "id",
                resource.id,
                "name",
                resource.name,
                "actions",
                JSON_ARRAYAGG(
                    JSON_OBJECT(
                        "id",
                        `action`.id,
                        "name",
                        `action`.name
                    )
                )
            ) AS resources_data
        FROM
            `role_permission`,
            `resource`,
            `action`
        WHERE
            `action`.id = `role_permission`.action_id AND `resource`.id = `role_permission`.resource_id AND `resource`.app_id = app_id
        GROUP BY
            resource.id
    ) AS resources
WHERE
    role.id = resources.role_id AND role.id = role_id AND role.app_id = app_id
GROUP BY
    role.id$$
DELIMITER ;