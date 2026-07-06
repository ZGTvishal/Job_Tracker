Phase 1 - Project Statement
"Maintain the current state of every job application by processing emails received from the email client"
    Business Flow -
        New Email
            |
        Store Email
            |
        Find Existing Application
                |----Exits---{Yes} -> Update status
                |          |---{No} -> Create Application
                |
                |
            Mark Email as processed

The project has two tables
        |- Email
        |- Application 

**Sequence**
1 - Store raw email in database 
2 - Extract 
    . Company
    . Role
    . Status signal
3 - Search for existing applications
4 - Not found -> create new application
5 - Set Status -> Applied
6 - Link email -> Application 
7 - Mark email as processed