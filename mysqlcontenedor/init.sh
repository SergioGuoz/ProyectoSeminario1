docker run --name docker_mysql \
-e MYSQL_ROOT_PASSWORD=admin \
-d mysql_f:0.1 \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci \
--default-authentication-plugin=mysql_native_password
