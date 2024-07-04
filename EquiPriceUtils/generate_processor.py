import json
import os
import random
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import QianfanLLMEndpoint
from flask import Blueprint, request, jsonify

generateProcessor = Blueprint('generate_report', __name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, '../static/data/law_clause.json')
corpus_file_path = os.path.join(current_dir, '../static/data/law_corpus.json')

with open(json_file_path, 'r', encoding='utf-8') as file:
    law_clauses = json.load(file)["clauses"]

with open(corpus_file_path, 'r', encoding='utf-8') as file:
    custom_corpus = json.load(file)


# 创建提示词模板
prompt_template = """
使用下面的语料来回答本模板最末尾的问题。
你需要将输入的话以第一人称的视角（我）转述一遍，以我在xx平台开头，并且以根据xxx法律接着写法律依据。
因为这是生成法律申诉信息，所以需要正式一些。
并且末句不要出现有关建议的各种描述。
如果你不知道问题的答案，禁止随意编造答案。
为了保证答案尽可能简洁，你的回答必须不超过三句话，你的回答中不可以带有星号。

以下是语料：
<context>
{context}
</context>

Question: {input}
"""

# 将上下文数据格式化为字符串
context_data = "\n".join([f"{pair['input']}\n{pair['output']}\n" for pair in custom_corpus])

# 创建 ChatPromptTemplate
prompt_text = prompt_template.replace("{context}", context_data)
prompt = ChatPromptTemplate.from_template(prompt_text)
prompt.input_variables = ["context", "input"]

# 创建千帆 LLM 模型实例
os.environ["QIANFAN_AK"] = "CZ77oypZkPnjdVKbOBReobOv"
os.environ["QIANFAN_SK"] = "qgme7WjIK4S8wN8sEuIDngVez2m6JhG4"
llm = QianfanLLMEndpoint(temperature=0.9)

# 创建文档检索链
document_chain = create_stuff_documents_chain(llm, prompt)

class Report:
    def __init__(self, name="artemis", phn="000-0000-0000", id="000000000000000000",
                 ocur_time="2024-01-01T00:00:00", gri_type="default", description="null",
                 evi="null", relate_company="null"):
        self.name = name
        self.phn = phn
        self.id = id
        self.ocur_time = ocur_time
        self.gri_type = gri_type
        self.description = description_transform(description)
        self.evi = evi
        self.relate_company = relate_company
        # self.law = self.set_random_law()
        self.law = "《电子商务法》第十八条　电子商务经营者根据消费者的兴趣爱好、消费习惯等特征向其提供商品或者服务的搜索结果的，应当同时向该消费者提供不针对其个人特征的选项，尊重和平等保护消费者合法权益。"

    def set_random_law(self):
        return random.choice(law_clauses)

    def to_dict(self):
        return {
            'name': self.name,
            'phn': self.phn,
            'id': self.id,
            'ocur_time': self.ocur_time,
            'gri_type': self.gri_type,
            'description': self.description,
            'evi': self.evi,
            'relate_company': self.relate_company,
            'law': self.law
        }

# 创建一个包含 page_content 属性的对象
class Document:
    def __init__(self, page_content):
        self.page_content = page_content
        self.metadata = {}

# 将 context_data 转换为 Document 对象列表
documents = [Document(data) for data in context_data.split("\n")]

@generateProcessor.route("/generate_report", methods=['POST'])
def generate():
    data = request.get_json()
    data_cpy = Report()
    if 'name' in data:
        data_cpy.name = data['name']
    if 'phn' in data:
        data_cpy.phn = data['phn']
    if 'id' in data:
        data_cpy.id = data['id']
    if 'ocur_time' in data:
        data_cpy.ocur_time = data['ocur_time']
    if 'gri_type' in data:
        data_cpy.gri_type = data['gri_type']
    if 'description' in data:
        data_cpy.description = description_transform(data['description'])
    if 'evi' in data:
        data_cpy.evi = data['evi']
    if 'relate_company' in data:
        data_cpy.relate_company = data['relate_company']
    return jsonify(data_cpy.to_dict())


def description_transform(description):
    # result = document_chain.invoke({"context": documents, "input": description})
    result = "我是一名淘宝平台的铂金用户。最近，我在淘宝上选择了一款耳机想要购买，显示的价格是698元。然而，通过EquiPrice平台我发现，其他普通用户的价格为675元。根据《电子商务法》第十八条的规定，电子商务经营者应当尊重和平等保护消费者的合法权益，并提供不针对个人特征的选项。我怀疑淘宝平台利用我的消费习惯和用户等级，通过大数据对我进行了价格歧视，对我显示了更高的价格。这种行为侵犯了我的公平交易权和消费者权益。"
    return result
