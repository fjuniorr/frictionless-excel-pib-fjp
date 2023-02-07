from frictionless import Package, Resource, Layout
from frictionless.plugins.excel import ExcelDialect

dialect = ExcelDialect(sheet=2, fill_merged_cells=True)
layout = Layout(header_rows=[3, 4], header_join = '-', pick_fields = list(range(1,16)), pick_rows = list(range(1, 84))) # skip_rows=['<blank>']

dp = Package()
r = Resource('data/15.12_Anexo-Estatistico-PIBmg-2021-3-valores.xlsx', dialect=dialect, layout=layout)
r.infer()
dp.add_resource(r)
dp.to_json('datapackage.json')
