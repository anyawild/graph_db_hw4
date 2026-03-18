/*
filename: graph_queries.sql

This file contains the SQL queries to answer the questions from Part 1,
with the outputs of each embedded as comments below.

Contributions: Anya Wild
*/


-- a. What is the sum of all book prices? Give just the sum.
SELECT SUM(num_value)
FROM node_props;

-- 253.45


-- b. Who does Spencer know? Give just their names.
SELECT string_value
FROM node_props
WHERE node_id in (SELECT out_node FROM edge 
    WHERE in_node IN (SELECT node_id FROM node_props WHERE string_value = 'Spencer')
    and type = 'knows');

-- Emily
-- Brendan


-- c. What books did Spencer buy? Give title and price.
SELECT string_value, num_value
FROM node_props
WHERE node_id in (SELECT out_node FROM edge 
    WHERE in_node IN (SELECT node_id FROM node_props WHERE string_value = 'Spencer')
    and type = 'bought');

-- Cosmos||17.0
-- Database Design||195.0


-- d. Who knows each other? Give just a pair of names.
SELECT string_value
FROM node_props
WHERE node_id in (SELECT out_node FROM edge 
    WHERE out_node in (SELECT in_node FROM edge WHERE type = 'knows') 
    and type = 'knows');

-- Emily
-- Spencer


-- e. Demonstrate a simple recommendation engine by answering the 
-- following question with a SQL query: What books were purchased
-- by people who Spencer knows? Exclude books that Spencer already owns.
SELECT string_value, num_value
FROM node_props
WHERE node_id in (SELECT out_node FROM edge 
    WHERE in_node IN (
        SELECT out_node FROM edge 
        WHERE in_node IN (SELECT node_id FROM node_props WHERE string_value = 'Spencer')
        and type = 'knows')
    and type = 'bought')
and node_id not in (SELECT out_node FROM edge 
    WHERE in_node IN (SELECT node_id FROM node_props WHERE string_value = 'Spencer')
    and type = 'bought');

-- DNA and you||11.5