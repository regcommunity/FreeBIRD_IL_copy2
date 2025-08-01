from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_01_02_REF_FINREP_3_0_UnionItem:
	base = None #F_01_02_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self) -> int:
		return self.base.CRRYNG_AMNT()
	@lineage(dependencies={"base.ACCNTNG_CLSSFCTN"})
	def ACCNTNG_CLSSFCTN(self) -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		return self.base.ACCNTNG_CLSSFCTN()
	@lineage(dependencies={"base.HLD_SL_INDCTR"})
	def HLD_SL_INDCTR(self) -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		return self.base.HLD_SL_INDCTR()
	@lineage(dependencies={"base.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self) -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		return self.base.SBJCT_IMPRMNT_INDCTR()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
	@lineage(dependencies={"base.TYP_HDG"})
	def TYP_HDG(self) -> str:
		''' return string from TYP_HDG enumeration '''
		return self.base.TYP_HDG()
	@lineage(dependencies={"base.TYP_ACCNTNG_ITM"})
	def TYP_ACCNTNG_ITM(self) -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		return self.base.TYP_ACCNTNG_ITM()

class F_01_02_REF_FINREP_3_0_Base:
	def CRRYNG_AMNT() -> int:
		pass
	def ACCNTNG_CLSSFCTN() -> str:
		''' return string from ACCNTNG_CLSSFCTN enumeration '''
		pass
	def HLD_SL_INDCTR() -> str:
		''' return string from HLD_SL_INDCTR enumeration '''
		pass
	def SBJCT_IMPRMNT_INDCTR() -> str:
		''' return string from SBJCT_IMPRMNT_INDCTR enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		pass
	def TYP_HDG() -> str:
		''' return string from TYP_HDG enumeration '''
		pass
	def TYP_ACCNTNG_ITM() -> str:
		''' return string from TYP_ACCNTNG_ITM enumeration '''
		pass

class F_01_02_REF_FINREP_3_0_UnionTable :
	F_01_02_REF_FINREP_3_0_UnionItems = [] # F_01_02_REF_FINREP_3_0_UnionItem []
	F_01_02_REF_FINREP_3_0_Deposits_Table = None # Deposits
	F_01_02_REF_FINREP_3_0_Deferred_tax_liabilities_Table = None # Deferred_tax_liabilities
	F_01_02_REF_FINREP_3_0_Provisions_Table = None # Provisions
	F_01_02_REF_FINREP_3_0_Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligations_Table = None # Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligations
	F_01_02_REF_FINREP_3_0_Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligations_Table = None # Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligations
	F_01_02_REF_FINREP_3_0_Provisions_Funds_for_general_banking_risks_Table = None # Provisions_Funds_for_general_banking_risks
	F_01_02_REF_FINREP_3_0_Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemes_Table = None # Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemes
	F_01_02_REF_FINREP_3_0_Provisions_Pending_legal_issues_and_tax_litigation_Table = None # Provisions_Pending_legal_issues_and_tax_litigation
	F_01_02_REF_FINREP_3_0_Provisions_Restructuring_Table = None # Provisions_Restructuring
	F_01_02_REF_FINREP_3_0_Share_capital_repayable_on_demand_Table = None # Share_capital_repayable_on_demand
	F_01_02_REF_FINREP_3_0_Tax_liabilities_Table = None # Tax_liabilities
	F_01_02_REF_FINREP_3_0_Other_financial_liabilities_Table = None # Other_financial_liabilities
	def calc_F_01_02_REF_FINREP_3_0_UnionItems(self) -> list[F_01_02_REF_FINREP_3_0_UnionItem] :
		items = [] # F_01_02_REF_FINREP_3_0_UnionItem []
		for item in self.F_01_02_REF_FINREP_3_0_Deposits_Table.Depositss:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Deferred_tax_liabilities_Table.Deferred_tax_liabilitiess:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Provisions_Table.Provisionss:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligations_Table.Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligationss:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligations_Table.Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligationss:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Provisions_Funds_for_general_banking_risks_Table.Provisions_Funds_for_general_banking_riskss:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemes_Table.Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemess:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Provisions_Pending_legal_issues_and_tax_litigation_Table.Provisions_Pending_legal_issues_and_tax_litigations:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Provisions_Restructuring_Table.Provisions_Restructurings:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Share_capital_repayable_on_demand_Table.Share_capital_repayable_on_demands:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Tax_liabilities_Table.Tax_liabilitiess:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_01_02_REF_FINREP_3_0_Other_financial_liabilities_Table.Other_financial_liabilitiess:
			newItem = F_01_02_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_01_02_REF_FINREP_3_0_UnionItems = []
		self.F_01_02_REF_FINREP_3_0_UnionItems.extend(self.calc_F_01_02_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Deposits(F_01_02_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.INSTRMNT_RL.CRRYNG_AMNT
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR

class Deferred_tax_liabilities(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Provisions(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligations(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligations(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Provisions_Funds_for_general_banking_risks(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemes(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Provisions_Pending_legal_issues_and_tax_litigation(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Provisions_Restructuring(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Share_capital_repayable_on_demand(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Tax_liabilities(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_ASST = None # NN_FNNCL_ASST
	@lineage(dependencies={"NN_FNNCL_ASST.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_ASST.CRRYNG_AMNT

class Other_financial_liabilities(F_01_02_REF_FINREP_3_0_Base):
	NN_FNNCL_LBLTY = None # NN_FNNCL_LBLTY
	@lineage(dependencies={"NN_FNNCL_LBLTY.CRRYNG_AMNT"})
	def CRRYNG_AMNT(self):
		return self.NN_FNNCL_LBLTY.CRRYNG_AMNT

class F_01_02_REF_FINREP_3_0_Deposits_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	Depositss = []# Deposits[]
	def calc_Depositss(self) :
		items = [] # Deposits[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Depositss = []
		self.Depositss.extend(self.calc_Depositss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Deferred_tax_liabilities_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Deferred_tax_liabilitiess = []# Deferred_tax_liabilities[]
	def calc_Deferred_tax_liabilitiess(self) :
		items = [] # Deferred_tax_liabilities[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Deferred_tax_liabilitiess = []
		self.Deferred_tax_liabilitiess.extend(self.calc_Deferred_tax_liabilitiess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Provisions_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Provisionss = []# Provisions[]
	def calc_Provisionss(self) :
		items = [] # Provisions[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Provisionss = []
		self.Provisionss.extend(self.calc_Provisionss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligations_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligationss = []# Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligations[]
	def calc_Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligationss(self) :
		items = [] # Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligations[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligationss = []
		self.Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligationss.extend(self.calc_Provisions_Employee_benefits_Other_than_pension_and_other_post_employment_defined_benefit_obligationss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligations_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligationss = []# Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligations[]
	def calc_Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligationss(self) :
		items = [] # Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligations[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligationss = []
		self.Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligationss.extend(self.calc_Provisions_Employee_benefits_Pension_and_other_post_employment_defined_benefit_obligationss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Provisions_Funds_for_general_banking_risks_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Provisions_Funds_for_general_banking_riskss = []# Provisions_Funds_for_general_banking_risks[]
	def calc_Provisions_Funds_for_general_banking_riskss(self) :
		items = [] # Provisions_Funds_for_general_banking_risks[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Provisions_Funds_for_general_banking_riskss = []
		self.Provisions_Funds_for_general_banking_riskss.extend(self.calc_Provisions_Funds_for_general_banking_riskss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemes_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemess = []# Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemes[]
	def calc_Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemess(self) :
		items = [] # Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemes[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemess = []
		self.Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemess.extend(self.calc_Provisions_Other_than_commitments_and_guarantees_given_and_payment_commitments_to_resolution_funds_and_deposit_guarantee_schemess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Provisions_Pending_legal_issues_and_tax_litigation_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Provisions_Pending_legal_issues_and_tax_litigations = []# Provisions_Pending_legal_issues_and_tax_litigation[]
	def calc_Provisions_Pending_legal_issues_and_tax_litigations(self) :
		items = [] # Provisions_Pending_legal_issues_and_tax_litigation[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Provisions_Pending_legal_issues_and_tax_litigations = []
		self.Provisions_Pending_legal_issues_and_tax_litigations.extend(self.calc_Provisions_Pending_legal_issues_and_tax_litigations())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Provisions_Restructuring_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Provisions_Restructurings = []# Provisions_Restructuring[]
	def calc_Provisions_Restructurings(self) :
		items = [] # Provisions_Restructuring[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Provisions_Restructurings = []
		self.Provisions_Restructurings.extend(self.calc_Provisions_Restructurings())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Share_capital_repayable_on_demand_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Share_capital_repayable_on_demands = []# Share_capital_repayable_on_demand[]
	def calc_Share_capital_repayable_on_demands(self) :
		items = [] # Share_capital_repayable_on_demand[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Share_capital_repayable_on_demands = []
		self.Share_capital_repayable_on_demands.extend(self.calc_Share_capital_repayable_on_demands())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Tax_liabilities_Table:
	NN_FNNCL_ASST_Table = None # NN_FNNCL_ASST
	Tax_liabilitiess = []# Tax_liabilities[]
	def calc_Tax_liabilitiess(self) :
		items = [] # Tax_liabilities[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Tax_liabilitiess = []
		self.Tax_liabilitiess.extend(self.calc_Tax_liabilitiess())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_01_02_REF_FINREP_3_0_Other_financial_liabilities_Table:
	NN_FNNCL_LBLTY_Table = None # NN_FNNCL_LBLTY
	Other_financial_liabilitiess = []# Other_financial_liabilities[]
	def calc_Other_financial_liabilitiess(self) :
		items = [] # Other_financial_liabilities[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Other_financial_liabilitiess = []
		self.Other_financial_liabilitiess.extend(self.calc_Other_financial_liabilitiess())
		CSVConverter.persist_object_as_csv(self,True)
		return None

