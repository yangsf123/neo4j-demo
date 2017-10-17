#!/usr/bin/python3

from neo4j.v1 import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j","ysf_neo4j"))

def print_friends_of(name):
    with driver.session() as session:
        with session.begin_transaction() as tx:
            for record in tx.run("MATCH (a:Person)-[:KNOWS]->(f) " \
                    "WHERE a.name={name}" \
                    "RETURN f.name", name=name):
                print(record['f.name'])

print_friends_of("Alice")

def add_person(self,name):
    with self._driver.session() as session:
        session.write_transaction(self.create_person_node, name)
        return session.read_transaction(self.match_person_node,name)

@staticmethod
def create_person_node(tx,name):
    tx.run("CREATE (a:Person {name:$name})", name=name)
    return None

@staticmethod
def match_person_node(tx,name):
    result = tx.run("MATCH (a:Person {name:$name}) RETURN count(a)", name=name)
    return result.single()[0]

def get_people(self):
    with self._driver.session() as session:
        return session.read_transaction(self.match_person_nodes)

@staticmethod
def match_person_nodes(tx):
    result = tx.run("MATCH (a:Person) RETURN a.name ORDER BY a.name")
    return [record["a.name"] for record in result]


def add_employees(self, company_name):
    with self._driver.session() as session:
        employees = 0
        persons = session.read_transaction(self.match_person_nodes)

        for person in persons:
            employees += session.write_transaction(self.add_employss_to_company, person, company_name)


        return employees

@staticmethod
def add_employee_to_company(tx, person, company_name):
    tx.run("MATCH (emp:Person {name:$person_name}) " \
            "MERGE (com:Company {name:$company_name}) " \
            "MERGE (emp)-[:WORKS_FOR]->(com)",
            person_name = person["name"], company_name=company_name)

@staticmethod
def match_person_nodes(tx):
    return list(tx.run("MATCH (a:Person) RETURN a.name as name"))


