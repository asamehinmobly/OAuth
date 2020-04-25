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
                r2.id,
                "name",
                r2.name,
                "actions",
                JSON_ARRAYAGG(
                        `action`.name
                )
            ) AS resources_data
        FROM
            `role_permission`,
            `resource` AS r1,
            `resource` AS r2,
            `action`
        WHERE
            `action`.id = `role_permission`.action_id AND r1.id = `role_permission`.resource_id AND r1.app_id = app_id AND `role_permission`.`role_id` = role_id AND r1.id = r2.parent_id
        GROUP BY
            r2.id
    ) AS resources
WHERE
    role.id = resources.role_id AND role.id = role_id AND role.app_id = app_id
GROUP BY
    role.id$$
DELIMITER ;