from tabulate import tabulate
from dataclasses import dataclass

@dataclass
class Plan: #isi class Plan harus sama banyak dengan isi jenis plan
  plan_name: str
  can_stream: bool
  can_download: bool
  has_sd: bool
  has_hd: bool
  has_uhd: bool
  num_devices: int
  content: str
  price: int
  level: int
  

  def check_plan(self):
    data = [
        ["Service", ""],
        ["Plan name", u'\u2713' if self.plan_name else "-"], #u'\u2713' if ... else "-" cetak centang
        ["Can stream", u'\u2713' if self.can_stream else "-"],
        ["Can download", u'\u2713' if self.can_download else "-"],
        ["Has SD", u'\u2713' if self.has_sd else "-"],
        ["HAS HD", u'\u2713' if self.has_hd else "-"],
        ["Has UHD", u'\u2713' if self.has_uhd else "-"],
        ["Number of device", self.num_devices],
        ["Available content", self.content],
        ["Price", f"Rp. {self.price:,}"],

    ]

## Di bawah ini jika ingin melakukan penambahan dengan syarat boolean
   #if self.can_stream:
      #data.append(["Can stream", u'\u2713'])
    #else:
      #data.append(["Can stream", "-"])

    print(tabulate(data, headers="firstrow")) #baris pertama pada nilai data dijadikan header

basic_plan = Plan(
    can_stream=True,
    can_download=True,
    has_sd=True,
    has_hd=False,
    has_uhd=False,
    num_devices=1,
    content="3rd party Movie only",
    price=120_000,
    plan_name="Basic Plan",
    level=1
)

standard_plan = Plan(
    can_stream=True,
    can_download=True,
    has_sd=True,
    has_hd=True,
    has_uhd=False,
    num_devices=2,
    content="Basic Plan + Sports",
    price=160_000,
    plan_name="Standard Plan",
    level=2
)

premium_plan = Plan(
    can_stream=True,
    can_download=True,
    has_sd=True,
    has_hd=True,
    has_uhd=True,
    num_devices=4,
    content="Standard Plan + PacFlix Original Content",
    price=200_000,
    plan_name="Premium Plan",
    level=3
)