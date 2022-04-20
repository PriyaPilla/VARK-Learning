CREATE TABLE student(
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    learning_style VARCHAR NULL,
    notes_timeline VARCHAR NULL,
    notes_cause VARCHAR NULL,
    notes_end VARCHAR NULL,
    notes_events VARCHAR NULL,
    notes_statistics VARCHAR NULL
);