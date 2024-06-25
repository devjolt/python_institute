('sql injection', ['takes advantage of unsanitised input vulnerabilities','passes SQL commands through a web application for execution by a backend database', 'attacker uses malicious SQL queries to perform unauthorised actions', 'works because of impropper validation']),



('authenication bypass', ['log onto an application without providing a valid username and password', 'gain administrative privileges']),
('authorisation bypass', ['alter authorisation information', 'change auth information in database']),
('information disclosure', ['obtains sensitive information', 'breaches confidentiality of database']),
('compromised data integrity', ['deface a web page', 'insert malicious content onto a web page', 'alters contents of a web page']),
('compromised availability of data',['delete database information', 'delete logs','delete audit information']),
('remote code injection', ['compromise host OS'])


#Relational databases
#HTTP methods



('in-band SQL injection', ['an attacker uses the same communication channel to perform the attack and retrieve the results', 'commonly used', 'error based and UNION based are most common']),
('blind/inferrential SQL injection', ['not possible to retrieve result', 'attacker has no error mesages to help', 'takes longer to execute', 'result is returned in boolean form', 'attackers use true or false results to determine the structre or the database and data', 'no data transmitted through the web application']),
('out-of-band SQL injection', ['different communication channels such as email', 'difficult to perform', 'features of the database server used must be found by the attacker']),


#in band sql injection
('error-based sql injection', ['an attacker  intentionall uses bad inputs to return errors', 'output messages used to find vulnerabilities', 'attacker injects SQL queries designed to compromise data security']),
('system stored procedure', ['results from unsanitised inputs which dynamically construct statements']),
('illegal/logically incorrect queries', ['gaining knowledge by using incorrect requests', 'helps attacker understand structure of underlying database']),
('UNION SQL injection', ['used to append a malicious query to the requested query', 'can be checked for by adding a \' character to the the end of command']),
('tautology', ['using a conditional OR clause to make a WHERE condition true', 'can be used to bypass user authentication']),
('end-of-line-comment', ['uses --', 'can end a query prematurely', 'causes anything afterwards to be ignored']),
('in-line-comments', ['allows integration of multiple vulnerable inputs into a single query','allows an attacker to bypass blacklisting', 'allows an attacker to remove spaces', 'allows an attacker to determine database versions']),
('piggybacked query', ['injecting an additional malicious query into the original query', 'generally performed on batched SQL queries', 'uses ;']),

