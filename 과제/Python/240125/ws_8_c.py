class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
    
    
    
class Other(BaseModel):
    TYPE = 'Other Model'
    def __init__(self,company,company_name,description,created_at,updated_at):
        self.company = company
        self.company_name = company_name
        self.description = description
        self.updated_at = updated_at
        self.created_at = created_at
        # BaseModel.PK += 1 # 시작이 1이다.
    
    def save(self):
        print('데이터를 다른 장소에 저장합니다.')

class ExtendedModel(Other, Novel):
    PK = 2
    def __init__(self,extended_type):
        self.extended_type = extended_type
        
    def display_info(same):
        print(f'PK: {same.PK}, TYPE: {same.TYPE}, Exteded Type: {same.extended_type}')
       
    def save(same):
        print('데이터를 확장해서 저장합니다.')

        

ex = ExtendedModel('Exteded Type')
print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
ex.display_info()
ex.save()


