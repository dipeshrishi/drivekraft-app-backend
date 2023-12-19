Create Database drivekraft_backend_V2;
use drivekraft_backend_V2;

CREATE TABLE user (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    contactNumber VARCHAR(15),
    created TIMESTAMP,
    updated TIMESTAMP,
    firebaseId VARCHAR(255),
    roleId INT,
    balance DECIMAL(10, 2),
    isBlocked BOOLEAN,
    FOREIGN KEY (roleId) REFERENCES user_role(id)
);

