import GeoIP

gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

print(gi.country_code_by_name("210.125.84.116"))
