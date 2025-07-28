from pybirdai.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.process_steps.pybird.csv_converter import CSVConverter
from datetime import datetime
from pybirdai.annotations.decorators import lineage

class F_41_01_REF_FINREP_3_0_UnionItem:
	base = None #F_41_01_REF_FINREP_3_0_Base
	@lineage(dependencies={"base.FV_HRRCHY"})
	def FV_HRRCHY(self) -> str:
		''' return string from FV_HRRCHY enumeration '''
		return self.base.FV_HRRCHY()
	@lineage(dependencies={"base.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self) -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		return self.base.TYP_INSTRMNT()
	@lineage(dependencies={"base.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self) -> str:
		''' return string from NGTBL_SCRTY enumeration '''
		return self.base.NGTBL_SCRTY_INDCTR()
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

class F_41_01_REF_FINREP_3_0_Base:
	def FV_HRRCHY() -> str:
		''' return string from FV_HRRCHY enumeration '''
		pass
	def TYP_INSTRMNT() -> str:
		''' return string from TYP_INSTRMNT enumeration '''
		pass
	def NGTBL_SCRTY_INDCTR() -> str:
		''' return string from NGTBL_SCRTY enumeration '''
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

class F_41_01_REF_FINREP_3_0_UnionTable :
	F_41_01_REF_FINREP_3_0_UnionItems = [] # F_41_01_REF_FINREP_3_0_UnionItem []
	F_41_01_REF_FINREP_3_0_Deposits_Table = None # Deposits
	F_41_01_REF_FINREP_3_0_Other_loans_Table = None # Other_loans
	F_41_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None # Non_Negotiable_bonds
	def calc_F_41_01_REF_FINREP_3_0_UnionItems(self) -> list[F_41_01_REF_FINREP_3_0_UnionItem] :
		items = [] # F_41_01_REF_FINREP_3_0_UnionItem []
		for item in self.F_41_01_REF_FINREP_3_0_Deposits_Table.Depositss:
			newItem = F_41_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_41_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss:
			newItem = F_41_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		for item in self.F_41_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss:
			newItem = F_41_01_REF_FINREP_3_0_UnionItem()
			newItem.base = item
			items.append(newItem)
		return items

	def init(self):
		Orchestration().init(self)
		self.F_41_01_REF_FINREP_3_0_UnionItems = []
		self.F_41_01_REF_FINREP_3_0_UnionItems.extend(self.calc_F_41_01_REF_FINREP_3_0_UnionItems())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class Deposits(F_41_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR

class Other_loans(F_41_01_REF_FINREP_3_0_Base):
	INSTRMNT = None # INSTRMNT
	@lineage(dependencies={"INSTRMNT.TYP_INSTRMNT"})
	def TYP_INSTRMNT(self):
		return self.INSTRMNT.TYP_INSTRMNT
	INSTRMNT_RL = None # INSTRMNT_RL
	@lineage(dependencies={"INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR"})
	def SBJCT_IMPRMNT_INDCTR(self):
		return self.INSTRMNT_RL.SBJCT_IMPRMNT_INDCTR
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR

class Non_Negotiable_bonds(F_41_01_REF_FINREP_3_0_Base):
	SCRTY_EXCHNG_TRDBL_DRVTV = None # SCRTY_EXCHNG_TRDBL_DRVTV
	@lineage(dependencies={"SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR"})
	def NGTBL_SCRTY_INDCTR(self):
		return self.SCRTY_EXCHNG_TRDBL_DRVTV.NGTBL_SCRTY_INDCTR

class F_41_01_REF_FINREP_3_0_Deposits_Table:
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


class F_41_01_REF_FINREP_3_0_Other_loans_Table:
	INSTRMNT_Table = None # INSTRMNT
	INSTRMNT_RL_Table = None # INSTRMNT_RL
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Other_loanss = []# Other_loans[]
	def calc_Other_loanss(self) :
		items = [] # Other_loans[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Other_loanss = []
		self.Other_loanss.extend(self.calc_Other_loanss())
		CSVConverter.persist_object_as_csv(self,True)
		return None


class F_41_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table:
	SCRTY_EXCHNG_TRDBL_DRVTV_Table = None # SCRTY_EXCHNG_TRDBL_DRVTV
	Non_Negotiable_bondss = []# Non_Negotiable_bonds[]
	def calc_Non_Negotiable_bondss(self) :
		items = [] # Non_Negotiable_bonds[
		# Join up any refered tables that you need to join
		# loop through the main table
		# set any references you want to on the new Item so that it can refer to themin operations
		return items
	def init(self):
		Orchestration().init(self)
		self.Non_Negotiable_bondss = []
		self.Non_Negotiable_bondss.extend(self.calc_Non_Negotiable_bondss())
		CSVConverter.persist_object_as_csv(self,True)
		return None

