# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cloudManager import CloudManager
import json
from loginSystem.models import Administrator

def router(request):
    try:
        data = json.loads(request.body)
        controller = data['controller']

        serverUserName = data['serverUserName']
        admin = Administrator.objects.get(userName=serverUserName)

        cm = CloudManager(data, admin)

        if controller == 'statusFunc':
            pass
        else:
            if cm.verifyLogin(request)[0] == 1:
                pass
            else:
                return cm.verifyLogin(request)[1]

        if controller == 'verifyLogin':
            return cm.verifyLogin(request)[1]
        elif controller == 'fetchWebsites':
            return cm.fetchWebsites()
        elif controller == 'fetchWebsiteDataJSON':
            return cm.fetchWebsiteDataJSON()
        elif controller == 'fetchWebsiteData':
            return cm.fetchWebsiteData()
        elif controller == 'submitWebsiteCreation':
            return cm.submitWebsiteCreation()
        elif controller == 'fetchModifyData':
            return cm.fetchModifyData()
        elif controller == 'saveModifications':
            return cm.saveModifications()
        elif controller == 'submitDBCreation':
            return cm.submitDBCreation()
        elif controller == 'fetchDatabases':
            return cm.fetchDatabases()
        elif controller == 'submitDatabaseDeletion':
            return cm.submitDatabaseDeletion()
        elif controller == 'changePassword':
            return cm.changePassword()
        elif controller == 'getCurrentRecordsForDomain':
            return cm.getCurrentRecordsForDomain()
        elif controller == 'deleteDNSRecord':
            return cm.deleteDNSRecord()
        elif controller == 'addDNSRecord':
            return cm.addDNSRecord()
        elif controller == 'submitEmailCreation':
            return cm.submitEmailCreation(request)
        elif controller == 'getEmailsForDomain':
            return cm.getEmailsForDomain(request)
        elif controller == 'submitEmailDeletion':
            return cm.submitEmailDeletion(request)
        elif controller == 'submitPasswordChange':
            return cm.submitPasswordChange(request)
        elif controller == 'fetchCurrentForwardings':
            return cm.fetchCurrentForwardings(request)
        elif controller == 'submitForwardDeletion':
            return cm.submitForwardDeletion(request)
        elif controller == 'submitEmailForwardingCreation':
            return cm.submitEmailForwardingCreation(request)
        elif controller == 'fetchDKIMKeys':
            return cm.fetchDKIMKeys(request)
        elif controller == 'generateDKIMKeys':
            return cm.generateDKIMKeys(request)
        elif controller == 'submitFTPCreation':
            return cm.submitFTPCreation(request)
        elif controller == 'getAllFTPAccounts':
            return cm.getAllFTPAccounts(request)
        elif controller == 'submitFTPDelete':
            return cm.submitFTPDelete(request)
        elif controller == 'changeFTPPassword':
            return cm.changeFTPPassword(request)
        elif controller == 'issueSSL':
            return cm.issueSSL(request)
        elif controller == 'submitWebsiteDeletion':
            return cm.submitWebsiteDeletion(request)
        elif controller == 'statusFunc':
            return cm.statusFunc()
        elif controller == 'submitDomainCreation':
            return cm.submitDomainCreation()
        elif controller == 'fetchDomains':
            return cm.fetchDomains()
        elif controller == 'submitDomainDeletion':
            return cm.submitDomainDeletion()
        elif controller == 'changeOpenBasedir':
            return cm.changeOpenBasedir()
        elif controller == 'changePHP':
            return cm.changePHP()
        elif controller == 'backupStatusFunc':
            return cm.backupStatusFunc()
        elif controller == 'submitBackupCreation':
            return cm.submitBackupCreation()
        elif controller == 'getCurrentBackups':
            return cm.getCurrentBackups()
        elif controller == 'deleteBackup':
            return cm.deleteBackup()
        elif controller == 'fetchACLs':
            return cm.fetchACLs()
        elif controller == 'submitUserCreation':
            return cm.submitUserCreation(request)
        elif controller == 'fetchUsers':
            return cm.fetchUsers()
        elif controller == 'submitUserDeletion':
            return cm.submitUserDeletion(request)
        elif controller == 'saveModificationsUser':
            return cm.saveModificationsUser(request)
        elif controller == 'userWithResellerPriv':
            return cm.userWithResellerPriv()
        elif controller == 'saveResellerChanges':
            return cm.saveResellerChanges(request)
        elif controller == 'changeACLFunc':
            return cm.changeACLFunc(request)
        elif controller == 'createACLFunc':
            return cm.createACLFunc(request)
        elif controller == 'findAllACLs':
            return cm.findAllACLs(request)
        elif controller == 'deleteACLFunc':
            return cm.deleteACLFunc(request)
        elif controller == 'fetchACLDetails':
            return cm.fetchACLDetails(request)
        elif controller == 'submitACLModifications':
            return cm.submitACLModifications(request)
        elif controller == 'submitPackage':
            return cm.submitPackage(request)
        elif controller == 'fetchPackages':
            return cm.fetchPackages(request)
        elif controller == 'submitPackageDelete':
            return cm.submitPackageDelete(request)
        elif controller == 'submitPackageModify':
            return cm.submitPackageModify(request)
        elif controller == 'getDataFromLogFile':
            return cm.getDataFromLogFile(request)
        elif controller == 'fetchErrorLogs':
            return cm.fetchErrorLogs(request)
        elif controller == 'submitApplicationInstall':
            return cm.submitApplicationInstall(request)
        elif controller == 'obtainServer':
            return cm.obtainServer(request)
        elif controller == 'getSSHConfigs':
            return cm.getSSHConfigs()
        elif controller == 'saveSSHConfigs':
            return cm.saveSSHConfigs()
        elif controller == 'deleteSSHKey':
            return cm.deleteSSHKey()
        elif controller == 'addSSHKey':
            return cm.addSSHKey()
        elif controller == 'getCurrentRules':
            return cm.getCurrentRules()
        elif controller == 'addRule':
            return cm.addRule()
        elif controller == 'deleteRule':
            return cm.deleteRule()
        elif controller == 'getLogsFromFile':
            return cm.getLogsFromFile(request)
        elif controller == 'serverSSL':
            return cm.serverSSL(request)
        else:
            return cm.ajaxPre(0, 'This function is not available in your version of CyberPanel.')

    except BaseException, msg:
        cm = CloudManager(None)
        return cm.ajaxPre(0, str(msg))
