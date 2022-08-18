from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, Text, String, DateTime, ForeignKey
from app.db.base_class import Base
from sqlalchemy.orm import relationship
from sqlalchemy import func


class Organization(Base):
    id = Column(Integer, primary_key=True, index=True)
    organization_name = Column(String, nullable=False)
    data_created = Column(DateTime, server_default=func.now())
    tests = relationship("TestData", back_populates="organization")

    __mapper_args__ = {"eager_defaults": True}

    def __str__(self):
        return self.organization_name

    class Config:
        orm_mode = True


class TestData(Base):
    id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String, nullable=False)
    extra_data = Column(Text)
    index_number = Column(Integer)
    introduction = Column(Text)
    data_created = Column(DateTime, default=datetime.utcnow())
    is_active = Column(Boolean, default=True)
    organization_id = Column(Integer, ForeignKey("organization.id"))
    organization = relationship("Organization", back_populates="tests")
    # questions = relationship("Question", back_populates="test")
    # questionaries = relationship("QuestionaryData", back_populates="test")

    def __str__(self):
        return self.test_name

    class Config:
        orm_mode = True


# class Question(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     question_type = Column(Integer, nullable=False)
#     question_text = Column(String, nullable=False)
#     index_number = Column(Integer)
#     data_created = Column(DateTime, default=datetime.utcnow())
#     is_active = Column(Boolean, default=True)
#     has_required_answer = Column(Boolean, default=True)
#     is_common_for_all_tests = Column(Boolean, default=False)
#     test_id = Column(Integer, ForeignKey("testdata.id"))
#     test = relationship("TestData", back_populates="questions")
#     answers_selectable = relationship("AnswerSelectable", back_populates="question")
#
#     def __str__(self):
#         return self.question_text + ' ' + str(self.question_type)
#
#     class Config:
#         orm_mode = True
#
#
# class AnswerSelectable(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     answer_text = Column(Text, nullable=False)
#     has_extra_data = Column(Boolean, default=False)
#     index_number = Column(Integer)
#     question_id = Column(Integer, ForeignKey("question.id"))
#     question = relationship("Question", back_populates="answers_selectable")
#
#     def __str__(self):
#         return self.answer_text
#
#     class Config:
#         orm_mode = True


# class QuestionaryData(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     data_created = Column(DateTime, default=datetime.utcnow())
#     extra_data = Column(Text)
#     test_id = Column(Integer, ForeignKey("testdata.id"))
#     test = relationship("TestData", back_populates="questionaries")
#     # results = relationship("TestResult", back_populates="questionary_data")
#
#     def __str__(self):
#         return self.test.test_name + ' ' + str(self.data_created)
#
#     class Config:
#         orm_mode = True


# class TestResult(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     answer_text = Column(Text)
#     answer_date = Column(DateTime)
#     extra_data = Column(Text)
#     questionary_id = Column(Integer, ForeignKey("questionarydata.id"))
#     # questionary = relationship("QuestionaryData", back_populates="results")
#     question_id = Column(Integer, ForeignKey("question.id"))
#     answer_selectable_id = Column(Integer, ForeignKey("answerselectable.id"))
#
#     def __str__(self):
#         return str(self.questionary_data)
#
#     class Config:
#         orm_mode = True
