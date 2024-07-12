CREATE DATABASE IF NOT EXISTS equipe_virtual;

USE equipe_virtual;

CREATE TABLE IF NOT EXISTS users (
    id_user BIGINT NOT NULL AUTO_INCREMENT,
    name_user VARCHAR(30) NOT NULL,
    email_user VARCHAR(50) NOT NULL,
    password_user VARCHAR(60) NOT NULL,
    PRIMARY KEY(id_user)
)

-- CREATE TABLE IF NOT EXISTS tools (
--     id_tool BIGINT NOT NULL AUTO_INCREMENT,
--     name_tool VARCHAR(30) NOT NULL,
--     PRIMARY KEY(id_tool)
-- )




CREATE TABLE IF NOT EXISTS crews (
    id_crew BIGINT NOT NULL AUTO_INCREMENT,
    name_crew VARCHAR(30),
    description_crew TEXT,
    process_crew VARCHAR(30),
    memory_crew BOOLEAN,
    cache_crew BOOLEAN,
    PRIMARY KEY(id_crew),
    iduser_crew BIGINT NOT NULL,
    FOREIGN KEY (iduser_crew) REFERENCES users (id_user)
)

CREATE TABLE IF NOT EXISTS tasks (
    id_task BIGINT NOT NULL AUTO_INCREMENT,
    name_task VARCHAR(30) NOT NULL,    
    description_task TEXT NOT NULL,
    status_task BOOLEAN,
    expected_output_task TEXT NOT NULL,    
    async_execution_task BOOLEAN,
    output_file_task VARCHAR(30),
    idcrew_task BIGINT NOT NULL,
    PRIMARY KEY(id_task),
    FOREIGN KEY (idcrew_task) REFERENCES crews (id_crew)
)

CREATE TABLE IF NOT EXISTS agents (
    id_agent BIGINT NOT NULL AUTO_INCREMENT,
    name_agent VARCHAR(30) NOT NULL,
    role_agent VARCHAR(30) NOT NULL,
    goal_agent TEXT,
    backstory_agent TEXT,
    llm_agent VARCHAR(30) DEFAULT 'gpt-4',
    llm_key_agent VARCHAR(60),
    allow_delegation_agent BOOLEAN,
    verbose_agent BOOLEAN,
    memory_agent BOOLEAN,
    idcrew_agent BIGINT NOT NULL,
    PRIMARY KEY(id_agent),
    FOREIGN KEY (idcrew_agent) REFERENCES crews (id_crew)
);

-- -----

-- INSERT INTO tools (name_tool)
-- VALUE("search_tool")



INSERT INTO users (
    name_user, email_user, password_user
)
VALUE(
    "augusto", "augustoomb@hotmail.com", "$2a$10$BsSTBeHRy8doQdnhrrJ16e.WoVEotyuZD2ZkQSeWqViHnSwapd0gu"
)

INSERT INTO crews (
    name_crew, description_crew, process_crew, memory_crew, cache_crew, iduser_crew
)
VALUE (
    "Equipe Legal",
    "Essa é uma breve descrição da equipe"
    "Process.sequential",
    TRUE,
    TRUE,
    1
)

INSERT INTO tasks (
    name_task, description_task, status_task, expected_output_task,
    async_execution_task, output_file_task, 
    idcrew_task
)
VALUE 
(   "Nome 1", "Identify the next big trend in technology. Focus on identifying pros and cons and the overall narrative.",
    1, "A comprehensive 3 paragraphs long report on the latest AI trends.",
    FALSE,
    "new-file.md",
    1
),
(   "Nome 2", "Identify2 the next big trend in technology. Focus on identifying pros and cons and the overall narrative.",
    1, "A comprehensive 3 paragraphs long report on the latest AI trends.",
    TRUE,
    "new-file2.md",
    1
),
(   "Nome 3", "Identify3 the next big trend in technology. Focus on identifying pros and cons and the overall narrative.",
    1, "A comprehensive 3 paragraphs long report on the latest AI trends.",
    TRUE,
    "new-file3.md",
    1
),


INSERT INTO agents (
    name_agent,
    role_agent,
    goal_agent,
    backstory_agent,
    llm_agent,
    llm_key_agent,
    allow_delegation_agent,
    verbose_agent,
    memory_agent,
    idcrew_agent
)
VALUE(
    "Pedro",
    "Senior developer",
    "Desenvolver soluções front-end next.js usando as melhores práticas",
    "Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world.",
    "gpt-3.5",
    "aosdihfiohasodifhasd787asjdhfi",
    TRUE,
    TRUE,
    TRUE,
    1
)