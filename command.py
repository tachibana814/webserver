# coding=utf-8
import json
import xmltodict
import sqlite3
import os


def file_name(file_dir):

    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        print(files)
        return files


def sub_file_path(file_dir):
    for dirs in os.walk(file_dir):
        # print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        return dirs


def xml_to_json(file):
    with open(file, 'r') as f:
        xml_str = f.read()
    xml_parse = xmltodict.parse(xml_str)
    json_str = json.dumps(xml_parse, indent=1)
    update_json = json_str.replace("@", "")
    # print(update_json)
    data = json.loads(update_json)
    # print(type(data))
    return data


def bha_id():
    sql_a = '''
            select last_insert_rowid() from BHAData
            '''
    cursor.execute(sql_a)
    return cursor.lastrowid


def survey_id():
    sql_b = '''
    select last_insert_rowid() from Survey
    '''
    cursor.execute(sql_b)
    return cursor.lastrowid


conn = sqlite3.connect('BHA.db')
cursor = conn.cursor()


class BHAData:
    def __init__(self, data):
        self.CaseFile = file_name
        self.ProductName = data['BHAData']['ProductName']
        self.ProductVersion = data['BHAData']['ProductVersion']
        self.SaveDate = data['BHAData']['SaveDate']
        self.ComputerName = data['BHAData']['ComputerName']
        self.UserName = data['BHAData']['UserName']
        self.OSName = data['BHAData']['OSName']
        self.CurrentCulture = data['BHAData']['CurrentCulture']
        self.DataVersion = data['BHAData']['DataVersion']
        self.ClassType = data['BHAData']['ClassType']

    def update_data(self, file):
        sql = ''' insert into BHAData
                      (
                      CaseFile,
                      ProductName,
                      ProductVersion,
                      SaveDate,
                      ComputerName,
                      UserName,
                      CurrentCulture,
                      DataVersion,
                      ClassType)
                      values
                      (
                      :str_CaseFile,
                      :str_ProductName,
                      :str_ProductVersion,
                      :str_SaveDate,
                      :str_ComputerName,
                      :str_UserName,
                      :str_CurrentCulture,
                      :str_DataVersion,
                      :str_ClassType)'''
        cursor.execute(sql, {
            'str_CaseFile': file,
            'str_ProductName': self.ProductName,
            'str_ProductVersion': self.ProductVersion,
            'str_SaveDate': self.SaveDate,
            'str_ComputerName': self.ComputerName,
            'str_UserName': self.UserName,
            'str_CurrentCulture': self.CurrentCulture,
            'str_DataVersion': self.DataVersion,
            'str_ClassType': self.ClassType})
        conn.commit()
        print("BHAData done")


class General:
    def __init__(self, data):
        self.ClassType = data['BHAData']['General']['ClassType']
        self.Date = data['BHAData']['General']['Date']
        self.Operator = data['BHAData']['General']['Operator']
        self.Well = data['BHAData']['General']['Well']
        self.Field = data['BHAData']['General']['Field']
        self.Rig = data['BHAData']['General']['Rig']
        self.Country = data['BHAData']['General']['Country']
        self.Contractor = data['BHAData']['General']['Contractor']
        self.Job = data['BHAData']['General']['Job']
        self.By = data['BHAData']['General']['By']
        self.Comments = data['BHAData']['General']['Comments']
        self.UserLogoChecked = data['BHAData']['General']['UserLogoChecked']
        self.UserLogo = data['BHAData']['General']['UserLogo']
        self.ClientLogoChecked = data['BHAData']['General']['ClientLogoChecked']
        self.ClientLogo = data['BHAData']['General']['ClientLogo']
        self.WellLocation = data['BHAData']['General']['WellLocation']
        self.AirGap = data['BHAData']['General']['AirGap']
        self.WaterDepth = data['BHAData']['General']['WaterDepth']
        self.SubseaWellheadChecked = data['BHAData']['General']['SubseaWellheadChecked']
        self.Index = data['BHAData']['General']['Index']

    def update_data(self, bha_id, file):
        # a = bha_id()
        # print('general-' +'bha_id'+ str(a))
        sql = ''' insert into General
                                      (
                                      BHA_ID,
                                      CaseFile,
                                      ClassType, 
                                      Date, 
                                      Operator, 
                                      Well, 
                                      Field, 
                                      Rig, 
                                      Country, 
                                      Contractor,
                                      Job,
                                      "By",
                                      Comments,
                                      UserLogoChecked,
                                      UserLogo,
                                      ClientLogoChecked,
                                      ClientLogo,
                                      WellLocation,
                                      AirGap,
                                      WaterDepth,
                                      SubseaWellheadChecked
                                      )
                                      values
                                      (
                                      :str_BHA_ID,
                                      :str_Case_File,
                                      :str_ClassType, 
                                      :str_Date, 
                                      :str_Operator, 
                                      :str_Well, 
                                      :str_Field, 
                                      :str_Rig, 
                                      :str_Country,
                                      :str_Contractor,
                                      :str_Job,
                                      :str_By,
                                      :str_Comments,
                                      :str_UserLogoChecked,
                                      :str_UserLogo,
                                      :str_ClientLogoChecked,
                                      :str_ClientLogo,
                                      :str_WellLocation,
                                      :str_AirGap,
                                      :str_WaterDepth,
                                      :str_SubseaWellheadChecked
                                      )'''
        cursor.execute(sql, {
            'str_BHA_ID': bha_id,
            'str_Case_File': file,
            'str_ClassType': self.ClassType,
            'str_Date': self.Date,
            'str_Operator': self.Operator,
            'str_Well': self.Well,
            'str_Field': self.Field,
            'str_Rig': self.Rig,
            'str_Country': self.Country,
            'str_Contractor': self.Contractor,
            'str_Job': self.Job,
            'str_By': self.By,
            'str_Comments': self.Comments,
            'str_UserLogoChecked': self.UserLogoChecked,
            'str_UserLogo': self.UserLogo,
            'str_ClientLogoChecked': self.ClientLogoChecked,
            'str_ClientLogo': self.ClientLogo,
            'str_WellLocation': self.WellLocation,
            'str_AirGap': self.AirGap,
            'str_WaterDepth': self.WaterDepth,
            'str_SubseaWellheadChecked': self.SubseaWellheadChecked})
        conn.commit()
        print(str(bha_id)+"general done")


class Survey:
    def __init__(self, data):
        self.ClassType = data['BHAData']['Survey']['ClassType']
        self.AnnotationChecked = data['BHAData']['Survey']['AnnotationChecked']
        self.TortuosityChecked = data['BHAData']['Survey']['TortuosityChecked']
        self.ProjectAziChecked = data['BHAData']['Survey']['ProjectAziChecked']
        self.ProjectAzi = data['BHAData']['Survey']['ProjectAzi']
        self.MaxTortuosity = data['BHAData']['Survey']['MaxTortuosity']
        self.Index = data['BHAData']['Survey']['Index']

    def update_data(self, bha_id):
        # a = bha_id()
        # print('survey' + str(a))
        sql = ''' insert into Survey
                              (
                              BHA_ID,
                              ClassType, 
                              AnnotationChecked, 
                              TortuosityChecked, 
                              ProjectAziChecked, 
                              ProjectAzi, 
                              MaxTortuosity
                              )
                              values
                              (
                              :str_BHA_ID,
                              :str_ClassType, 
                              :str_AnnotationChecked, 
                              :str_TortuosityChecked, 
                              :str_ProjectAziChecked, 
                              :str_ProjectAzi, 
                              :str_MaxTortuosity
                              )'''
        cursor.execute(sql, {
                            'str_BHA_ID': bha_id,
                            'str_ClassType': self.ClassType,
                            'str_AnnotationChecked': self.AnnotationChecked,
                            'str_TortuosityChecked': self.TortuosityChecked,
                            'str_ProjectAziChecked': self.ProjectAziChecked,
                            'str_ProjectAzi': self.ProjectAzi,
                            'str_MaxTortuosity': self.MaxTortuosity})
        conn.commit()
        print(str(bha_id)+"Survey done")


class SurveyRow:
    def __init__(self, data):
        self.ClassType = []
        self.MD = []
        self.Inc = []
        self.Azi = []
        self.Index = []
        if 'SurveyRow' in data['BHAData']['Survey']['Survey']:
            for row in data['BHAData']['Survey']['Survey']['SurveyRow']:
                self.ClassType.append(row['ClassType'])
                self.MD.append(row['MD'])
                self.Inc.append(row['Inc'])
                self.Azi.append(row['Azi'])
                self.Index.append(row['Index'])

    def update_data(self, bha_id, survey_id):
        # b = survey_id()
        sql = ''' insert into SurveyRow
                                      (
                                      BHA_ID,
                                      SurveyID,
                                      ClassType, 
                                      MD, 
                                      Inc, 
                                      Azi
                                      )
                                      values
                                      (
                                      :str_BHA_ID,
                                      :str_SurveyID,
                                      :str_ClassType, 
                                      :str_MD, 
                                      :str_Inc, 
                                      :str_Azi
                                      )'''
        for i in range(0, len(self.ClassType)):
            cursor.execute(sql, {
                'str_BHA_ID': bha_id,
                'str_SurveyID': survey_id,
                'str_ClassType': self.ClassType[i],
                'str_MD': self.MD[i],
                'str_Inc': self.Inc[i],
                'str_Azi': self.Azi[i]})
            conn.commit()
        print(str(bha_id)+"survey row done")


class AnnotationRow:
    def __init__(self, data):
        self.ClassType = []
        self.MD = []
        self.Annotation = []
        self.Symbol = []
        self.Index = []
        if 'AnnotationRow' in data['BHAData']['Survey']['Annotation']:
            for row in data['BHAData']['Survey']['Annotation']['AnnotationRow']:
                self.ClassType.append(row['ClassType'])
                self.MD.append(row['MD'])
                self.Annotation.append(row['Annotation'])
                self.Symbol.append(row['Symbol'])
                self.Index.append(row['Index'])

    def update_data(self, survey_id):
        sql = ''' insert into AnnotationRow
                                              (
                                              SurveyID,
                                              ClassType, 
                                              MD, 
                                              Annotation, 
                                              Symbol
                                              )
                                              values
                                              (
                                              :str_SurveyID,
                                              :str_ClassType, 
                                              :str_MD, 
                                              :str_Annotation, 
                                              :str_Symbol
                                              )'''
        for i in range(0, len(self.ClassType)):
            cursor.execute(sql, {
                'str_SurveyID': survey_id,
                'str_ClassType': self.ClassType[i],
                'str_MD': self.MD[i],
                'str_Annotation': self.Annotation[i],
                'str_Symbol': self.Symbol[i]})
            conn.commit()
        print(str(bha_id)+"annotation row done")


class TortuosityRow:
    def __init__(self, data):
        self.ClassType = []
        self.From = []
        self.To = []
        self.Amplitude = []
        self.Period = []
        self.Interval = []
        self.Index = []
        if 'TortuosityRow' in data['BHAData']['Survey']['Tortuosity']:
            for row in data['BHAData']['Survey']['Tortuosity']['TortuosityRow']:
                self.ClassType.append(row['ClassType'])
                self.From.append(row['From'])
                self.To.append(row['To'])
                self.Amplitude.append(row['Amplitude'])
                self.Period.append(row['Period'])
                self.Interval.append(row['Interval'])
                self.Index.append(row['Index'])

    def update_data(self, survey_id):
        sql = ''' insert into TortuosityRow
                                              (
                                              SurveyID,
                                              ClassType, 
                                              From, 
                                              To, 
                                              Amplitude,
                                              Period,
                                              Interval
                                              )
                                              values
                                              (
                                              :str_SurveyID,
                                              :str_ClassType, 
                                              :str_From, 
                                              :str_To, 
                                              :str_Amplitude,
                                              :str_Period,
                                              :str_Interval
                                              )'''
        for i in range(0, len(self.ClassType)):
            cursor.execute(sql, {
                'str_SurveyID': survey_id,
                'str_ClassType': self.ClassType[i],
                'str_From': self.From[i],
                'str_To': self.To[i],
                'str_Amplitude': self.Amplitude[i],
                'str_Period': self.Period[i],
                'str_Interval': self.Interval[i]})
            conn.commit()
        print(str(bha_id)+"tortuosity row done")


class CasedHoleRow:
    def __init__(self, data):
        self.ClassType = []
        self.Bottom = []
        self.Description = []
        self.InnerDiameter = []
        self.FrictionFactor = []
        self.Index = []
        if 'CasedHoleRow' in data['BHAData']['Wellbore']['CasedHole']:
            for row in data['BHAData']['Wellbore']['CasedHole']['CasedHoleRow']:
                self.ClassType.append(row['ClassType'])
                self.Bottom.append(row['Bottom'])
                self.Description.append(row['Description'])
                self.InnerDiameter.append(row['InnerDiameter'])
                self.FrictionFactor.append(row['FrictionFactor'])
                self.Index.append(row['Index'])

    def update_data(self, bha_id):
        sql = ''' insert into CasedHoleRow
                                                      (
                                                      BHA_ID,
                                                      ClassType, 
                                                      Bottom, 
                                                      Description, 
                                                      InnerDiameter,
                                                      FrictionFactor
                                                      )
                                                      values
                                                      (
                                                      :str_BHA_ID,
                                                      :str_ClassType, 
                                                      :str_Bottom, 
                                                      :str_Description, 
                                                      :str_InnerDiameter,
                                                      :str_FrictionFactor
                                                      )'''
        for i in range(0, len(self.ClassType)):
            cursor.execute(sql, {
                'str_BHA_ID': bha_id,
                'str_ClassType': self.ClassType[i],
                'str_Bottom': self.Bottom[i],
                'str_Description': self.Description[i],
                'str_InnerDiameter': self.InnerDiameter[i],
                'str_FrictionFactor': self.FrictionFactor[i]})
            conn.commit()
        print(str(bha_id)+"CasedHoleRow done")


class OpenHoleRow:
    def __init__(self, data):
        self.ClassType = []
        self.Bottom = []
        self.Description = []
        self.InnerDiameter = []
        self.FrictionFactor = []
        self.Index = []
        if 'OpenHoleRow' in data['BHAData']['Wellbore']['OpenHole']:
            for row in data['BHAData']['Wellbore']['OpenHole']['OpenHoleRow']:
                self.ClassType.append(row['ClassType'])
                self.Bottom.append(row['Bottom'])
                self.Description.append(row['Description'])
                self.InnerDiameter.append(row['InnerDiameter'])
                self.FrictionFactor.append(row['FrictionFactor'])
                self.Index.append(row['Index'])

    def update_data(self, bha_id):
        sql = ''' insert into OpenHoleRow
                                                      (
                                                      BHA_ID,
                                                      ClassType, 
                                                      Bottom, 
                                                      Description, 
                                                      InnerDiameter,
                                                      FrictionFactor
                                                      )
                                                      values
                                                      (
                                                      :str_BHA_ID,
                                                      :str_ClassType, 
                                                      :str_Bottom, 
                                                      :str_Description, 
                                                      :str_InnerDiameter,
                                                      :str_FrictionFactor
                                                      )'''
        for i in range(0, len(self.ClassType)):
            cursor.execute(sql, {
                'str_BHA_ID': bha_id,
                'str_ClassType': self.ClassType[i],
                'str_Bottom': self.Bottom[i],
                'str_Description': self.Description[i],
                'str_InnerDiameter': self.InnerDiameter[i],
                'str_FrictionFactor': self.FrictionFactor[i]})
            conn.commit()
        print(str(bha_id)+"OpenHoleRow done")


# class Operation:
#     def __init__(self, data):
#         self.ClassType = data['BHAData']['Operation']['ClassType']
#         self.DepthOfInterest = data['BHAData']['Operation']['DepthOfInterest']
#         self.Index = data['BHAData']['Operation']['Index']


class OperationRow:
    def __init__(self, data):
        self.ClassType = []
        self.Description = []
        self.EndingDepth = []
        self.MW = []
        self.WOB = []
        self.TOB = []
        self.ROP = []
        self.RPM = []
        self.FrictionFactor = []
        self.Index = []
        if 'OperationRow' in data['BHAData']['Operation']['Operation']['OperationRow']:
            for row in data['BHAData']['Operation']['Operation']['OperationRow']:
                self.ClassType.append(row['ClassType'])
                self.Description.append(row['Description'])
                self.EndingDepth.append(row['EndingDepth'])
                self.MW.append(row['MW'])
                self.WOB.append(row['WOB'])
                self.TOB.append(row['TOB'])
                self.ROP.append(row['ROP'])
                self.RPM.append(row['RPM'])
                self.FrictionFactor.append(row['FrictionFactor'])
                self.Index.append(row['Index'])

    def update_data(self, bha_id):
        sql = ''' insert into OperationRow
                                                              (
                                                              BHA_ID,
                                                              Description, 
                                                              EndingDepth, 
                                                              MW,
                                                              WOB,
                                                              TOB,
                                                              ROP,
                                                              RPM,
                                                              FrictionFactor
                                                              )
                                                              values
                                                              (
                                                              :str_BHA_ID,
                                                              :str_Description, 
                                                              :str_EndingDepth, 
                                                              :str_MW, 
                                                              :str_WOB,
                                                              :str_TOB,
                                                              :str_ROP,
                                                              :str_RPM,
                                                              :str_FrictionFactor
                                                              )'''
        for i in range(0, len(self.Description)):
            cursor.execute(sql, {
                'str_BHA_ID': bha_id,
                'str_Description': self.Description[i],
                'str_EndingDepth': self.EndingDepth[i],
                'str_MW': self.MW[i],
                'str_WOB': self.WOB[i],
                'str_TOB': self.TOB[i],
                'str_ROP': self.ROP[i],
                'str_RPM': self.RPM[i],
                'str_FrictionFactor': self.FrictionFactor[i]})
            conn.commit()
        print(str(bha_id)+"operation_row done")

#
# class BHA:
#     def __init__(self, data):
#         self.ClassType = data['BHAData']['BHA']['ClassType']
#         self.ComponentOfInterest = data['BHAData']['BHA']['ComponentOfInterest']
#         self.Index = data['BHAData']['BHA']['Index']


class BHAComponentRow:
    def __init__(self, data):
        self.ClassType = []
        self.Description = []
        self.Type = []
        self.Index = []
        if 'BHAComponentRow' in data['BHAData']['BHA']['BHA']:
            for row in data['BHAData']['BHA']['BHA']['BHAComponentRow']:
                self.ClassType.append(row['ClassType'])
                self.Description.append(row['Description'])
                self.Type.append(row['Type'])
                self.Index.append(row['Index'])

    def update_data(self, bha_id):
        sql = ''' insert into BHAComponentRow
                                                                      (
                                                                      BHA_ID,
                                                                      ClassType, 
                                                                      Description, 
                                                                      Type
                                                                      )
                                                                      values
                                                                      (
                                                                      :str_BHA_ID,
                                                                      :str_ClassType, 
                                                                      :str_Description, 
                                                                      :str_Type
                                                                      )'''
        for i in range(0, len(self.Description)):
            cursor.execute(sql, {
                'str_BHA_ID': bha_id,
                'str_ClassType': self.ClassType[i],
                'str_Description': self.Description[i],
                'str_Type': self.Type[i]})
            conn.commit()
        print(str(bha_id)+"BHAComponentRow done")


class BHAComponent:
    def __init__(self, data):
        self.ClassType = []
        self.Size = []
        self.Wt = []
        self.Length = []
        self.MakeupTorque = []
        for row in data['BHAData']['BHA']['BHA']['BHAComponentRow']:
            if row['Type'] == 'Bit':
                self.ClassType.append(row['BHAComponet']['ClassType'])
                self.Size.append(row['BHAComponet']['Size'])
                self.Wt.append(row['BHAComponet']['Wt'])
                self.Length.append(row['BHAComponet']['Length'])
                self.MakeupTorque.append(row['BHAComponet']['MakeupTorque'])
        # print(self.ClassType)
        # print(self.Size)
        # print(self.Wt)
        # print(self.Length)
        # print(self.MakeupTorque)

    def update_data(self, bha_id):
        sql = ''' insert into BHAComponent
                                                                      (
                                                                      BHA_ID,
                                                                      ClassType, 
                                                                      Size, 
                                                                      Wt,
                                                                      Length,
                                                                      MakeupTorque
                                                                      )
                                                                      values
                                                                      (
                                                                      :str_BHA_ID,
                                                                      :str_ClassType, 
                                                                      :str_Size, 
                                                                      :str_Wt,
                                                                      :str_Length,
                                                                      :str_MakeupTorque
                                                                      )'''
        for i in range(0, len(self.ClassType)):
            cursor.execute(sql, {
                'str_BHA_ID': bha_id,
                'str_ClassType': self.ClassType[i],
                'str_Size': self.Size[i],
                'str_Wt': self.Wt[i],
                'str_Length': self.Length[i],
                'str_MakeupTorque': self.MakeupTorque[i]})
            conn.commit()
        print(str(bha_id)+"BHAComponent done")


if __name__ == "__main__":
    # for i in range(1, 35):
    #         xml_to_json('{}.xml'.format(i))
    file_path = 'E:\\PVI\\BHA\\DB\\YG\\BHAPRO_test_5'
    files = file_name(file_path)
    # for sub_file_path in file_path_list:
    #     files = file_name(file_path+sub_file_path)
    for file in files:
        data = xml_to_json(file_path+"\\"+file)
        print(file_path +"\\"+file)
        # # # bha_data部分
        bha_data = BHAData(data)
        bha_data.update_data(file)
        # # # 获取bha_id主键
        a = bha_id()
        print('bha_id:' + str(a))
        # # # general部分
        gen = General(data)
        gen.update_data(a, file)
        # # Survey部分
        survey = Survey(data)
        survey.update_data(a)
        # # # 获取survey_id
        b = survey_id()
        print('survey_id:' + str(b))
        # # # survey_row部分
        survey_row = SurveyRow(data)
        survey_row.update_data(a,b)
        # # # annotation row
        annotation_Row = AnnotationRow(data)
        annotation_Row.update_data(b)
        # #
        # # # T
        tortuosity_row = TortuosityRow(data)
        tortuosity_row.update_data(b)
        # #
        # Cased Hole
        casedHole_row = CasedHoleRow(data)
        casedHole_row.update_data(a)
        # # # open hole
        openHole_row = OpenHoleRow(data)
        openHole_row.update_data(a)
        # #
        # operation row
        operation_row = OperationRow(data)
        operation_row.update_data(a)
        # #
        # BHA_component_row
        BHA_component_row = BHAComponentRow(data)
        BHA_component_row.update_data(a)

        # BHA_component
        BHA_component = BHAComponent(data)
        BHA_component.update_data(a)



