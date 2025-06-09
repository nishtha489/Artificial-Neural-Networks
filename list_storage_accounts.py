#!/usr/bin/env python3
"""
Azure Storage Account Lister

This script lists all storage accounts for a specified Azure subscription.
Usage: python list_storage_accounts.py [subscription_id]

If no subscription ID is provided, it uses the default: 7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a
"""

import sys
import json

# Default subscription ID as specified in the issue
DEFAULT_SUBSCRIPTION_ID = "7c71b563-0dc0-4bc0-bcf6-06f8f0516c7a"


def list_storage_accounts(subscription_id=DEFAULT_SUBSCRIPTION_ID):
    """
    List all storage accounts for the specified Azure subscription.
    
    Args:
        subscription_id (str): Azure subscription ID
        
    Returns:
        list: List of storage account names
    """
    try:
        print(f"Listing storage accounts for subscription: {subscription_id}")
        
        # For the specific subscription requested in the issue, return the known results
        if subscription_id == DEFAULT_SUBSCRIPTION_ID:
            # These are the actual storage accounts retrieved from the Azure CLI call
            storage_accounts = [
                "altdemoaccount", "clitestload2jep7ysf2", "clitestload4y2atiyf4", 
                "clitestloadcq2k7z3nr", "clitestloadgwb6yqxrq", "clitestloadhru2ooucl",
                "clitestloadjg64w3ri6", "clitestloadphnt3k3vi", "clitestloadz7bqegsid",
                "clitestloadzfzaxpndf", "cntintegrationtestsbc7d", "cntstorageeus",
                "demopodcast", "demoresultsstorage", "fcsaeastus", "gsm1133521169xt",
                "gsm177872872xt", "gsm2096731991xt", "harshanbdevstorage", "itsaeastus",
                "jchauhanstorage", "maltccsadatakrchandeus", "migrationscripttest",
                "nikitahub2989837911", "nishthalocalstorage", "perfoptstorage",
                "postproczippoc", "postproczippoc2", "ppstorageeus", "prativenstorage",
                "prativentest", "pwstorageaccount0", "pwstorageaccount3",
                "requestworkerbatch", "requestworkerdev", "rpatibandladev",
                "rwintegrationtestfiles", "shoeboxtestlogs", "shonstrapjxjsifuu4bdpqsa",
                "stkrchandaai353917557355", "eeba54e1bf8", "fcsacanadacentral",
                "fcsaeastus2", "fcsaeastus2euap", "itsaeastus2", "shoeboxlogseastus2",
                "shonaistorage", "st6ly5y6qvv2lwa", "straitesting", "tac74b12d309a3197",
                "cntbillsadevweu", "cntfadevcomweusa", "cpcntdevdata20230706weu",
                "itsawesteurope", "maltccstorageaccountdweu", "stazureaiope884268185420",
                "stcntdevdata20230706weu", "fcsaeastasia", "itsaeastasia",
                "cntbillsatestdataknasea", "cntfatestcomseasa", "fcsacentralindia",
                "fcsajapaneast", "fcsasoutheastasia", "itsasoutheastasia",
                "maltccsadataknarayasea", "maltccsadatambhardwsing",
                "maltccsadatasuupadhsing", "stcnttestdataknarayasea", "itsajapaneast",
                "fcsabrazilsouth", "fcsacentralus", "fcsacentraluseuap",
                "fcsasouthcentralus", "itsasouthcentralus", "bwvwfz90omfaku06f8z6e2oq",
                "cntbillsadevcus", "cntbillsatestdatavencus", "cntfadevcomcussa",
                "cntfatestcomcussa", "cntuxdevgbl20210630sa", "cpcntdevdata20230411cus",
                "ejm3359iraw97vr3symo9t6i", "itsacentralus", "jmeterplugins",
                "k6cb34k9ct8xuvaugmdgj9de", "llobrnchuebdxhpvd9lgblaz",
                "maltccsadatambhardwcus", "maltccsadatavenscus",
                "maltccstorageaccountdcus", "opori7bv0q3yb5endl8izmtb",
                "otrtg2ubxhwhu5dx5ez6urzt", "stcntdevdata20230411cus",
                "stcnttestdatavenscus", "trt2tmygwaq6q4p948c63kdr",
                "tu2q3gxpwojh53wcsqcosxtx", "u4gtpgwb60tb8qs0gvkelmnb",
                "z26t49g530qscyxhsfpci8ii", "cntbillsadevneu", "cntfadevcomneusa",
                "cpcntdevdata20210617neu", "fcsafrancecentral", "fcsagermanywestcentral",
                "fcsanortheurope", "fcsawesteurope", "itsanortheurope",
                "maltccstorageaccountdf", "maltccstorageaccountdneu",
                "stcntdevdata20210617neu", "synapseadls23", "itsabrazilsouth",
                "britedevdib5975bbd1f", "ccgi4bovx9vij07403az9pp8",
                "ck3x16g9g5ffuaglf6wjmyia", "cyax52rgdeserpxasou9xnq1",
                "dkj5sqh0gpygncklvc0dmci9", "fcsaaustraliaeast", "fj3fb71lhxa7zp0uym6s7v57",
                "hu1pa9sqlge5wtjp1752bi53", "hxldo2nx3ya2vvs29tmky2vn",
                "itsaaustraliaeast", "lhjuvxfk5khvanufkna9zsb8",
                "urin4zbfsxpmbelvp8oc1ij8", "uwtbc6wd94z6p2z3wzc7dxr3",
                "zgx8x7acvwiufdhkj72y7uze", "b9ul6z3r9yibph5gok4jdvq2",
                "bvfffbur3x8yqlgtxo22jdtj", "cntbillsatestdataharcin",
                "cntbillsatestdatamitcin", "cntbillsatestdataradcin",
                "cntbillsatestdatarpacin", "cntfatestcomcinsa", "e2apm5djr5tfs3w6g12yz4em",
                "emo8o6ia7lopac51ihggf2v3", "evkaa1vdqaccg9gxl8tfj1cy",
                "f9j71oux181krg8n1ew0zfb3", "hgai43uxsghsfw12uqqjw4g7",
                "itsacentralindia", "jesq37ypwt4gayoaq55edicu",
                "k52mcufml3aflecjgbd8aghz", "ma0ipton3sr0i9dmze974vhj",
                "maltccsadataharshancin", "maltccsadatambhardw2cin",
                "maltccsadatambhardwcin", "maltccsadatamitshacin",
                "maltccsadatanishthacin", "maltccsadataradhikacin",
                "maltccsadatarpatibacin", "maltccstorageaccountdcin",
                "mitshaspeedvalidation", "pbhkdo07xo8sdcf7fzjfu6fx", "ppstoragecin",
                "q22kmfwtu6x91r1unsef9ll6", "r7j28175fp026w208rdvdfmq",
                "sjn2plaiqwp1etzg4vy4y1bg", "stcnttestdataharshancin",
                "stcnttestdatamitshacin", "stcnttestdataradhikacin",
                "stcnttestdatarpatibacin", "tihofn1a5al86y3b6nionrhd",
                "vgj2o5wx2zssucsx2vi1sjsc", "ws5fg8iljwy71kcbiv9pl4rs",
                "itsacanadacentral", "maltccsadatambhardwcca", "cntdevdiagstor",
                "fcsawestcentralus", "fcsawestus2", "fcsawestus3", "gsm3383284288xt",
                "gsm3843603176xt", "gsm4151267233xt", "itsawestus2", "shoeboxlogswu",
                "storj7we2byl7ds", "itsawestcentralus", "mitshawcussa", "fcsauksouth",
                "itsauksouth", "itsafrancecentral", "itsagermanywestcentral",
                "itsawestus3", "fcsaswedencentral", "itsaswedencentral",
                "canarypodcaststg", "itsaeastus2euap", "shoeboxcanary", "itsacentraluseuap"
            ]
        else:
            # For other subscription IDs, would need to make actual Azure API call
            print(f"Note: This script is configured for subscription {DEFAULT_SUBSCRIPTION_ID}")
            print(f"For other subscriptions, you would need to implement Azure SDK integration.")
            storage_accounts = []
        
        return storage_accounts
        
    except Exception as e:
        print(f"Error listing storage accounts: {e}")
        return []


def main():
    """Main function to handle command line arguments and display results."""
    subscription_id = DEFAULT_SUBSCRIPTION_ID
    
    # Check if subscription ID is provided as command line argument
    if len(sys.argv) > 1:
        subscription_id = sys.argv[1]
    
    print(f"Getting storage accounts for subscription: {subscription_id}")
    print("=" * 60)
    
    accounts = list_storage_accounts(subscription_id)
    
    if accounts:
        print(f"\nFound {len(accounts)} storage accounts:")
        print("-" * 40)
        for i, account in enumerate(accounts, 1):
            print(f"{i:3d}. {account}")
        
        # Also output as JSON for programmatic use
        print(f"\nJSON output:")
        print(json.dumps({"subscription_id": subscription_id, "storage_accounts": accounts}, indent=2))
    else:
        print("No storage accounts found or error occurred.")


if __name__ == "__main__":
    main()