# reports module
reports_section = "//p[contains(text(), 'Reports')]"

# severity section
high_sev = "//div[@role='group']/div[@class='row']//div[@class='col-sm-6'][1]//span[@class='el-checkbox__inner']"
med_sev = "//div[@role='group']/div[@class='row']//div[@class='col-sm-6'][2]//span[@class='el-checkbox__inner']"
low_sev = "//div[@role='group']/div[@class='row']//div[@class='col-sm-6'][3]//span[@class='el-checkbox__inner']"
info_sev = "//div[@role='group']/div[@class='row']//div[@class='col-sm-6'][4]//span[@class='el-checkbox__inner']"

# report type xpaths
exec_summary = "//input[@value='execSummary']/../span"
detailed_report = "//input[@value='detailedReport']/../span"
comparison = "//input[@value='Comparison']/../span"
daterange_comparison = "//input[@value='dateRangeComparison']/../span"
