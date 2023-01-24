from dataclasses import dataclass
from datetime import datetime
from dateutil import relativedelta
from plan import Plan

@dataclass #decorator
class User:
  username: str
  plan: Plan
  start_subs_time: datetime
  referral_code: str=None #None: bisa diberikan input, bisa dilewatkan
  
  def __post_init__(self):
    self.invoice = self.plan.price

  def upgrade_plan(self, new_plan):
    # check if not downgrade
    if new_plan.level <= self.plan.level:
      print("Plan tidak boleh downgrade atau memilih upgrade ke level yang sama!")
      return #ketika sudah ketemu return, maka keluar dari function alias kembali.
    # discount 5% 
    # if start_subs_time > 12 months
    discount = 1
    difference = relativedelta.relativedelta(datetime.now(), self.start_subs_time)
    if difference.months > 12:
      discount = 0.95
    # change plan & start_subs_time
    self.plan = new_plan
    self.start_subs_time = datetime.now()
    self.invoice = self.plan.price * discount