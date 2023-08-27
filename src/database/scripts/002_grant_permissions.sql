use Terminus;

GO

CREATE LOGIN Finatial WITH PASSWORD = 'RT778%abZ1*';

GO

CREATE USER FinatialUser FOR LOGIN Finatial;

GO

GRANT SELECT ON Terminus.Manager TO FinatialUser;