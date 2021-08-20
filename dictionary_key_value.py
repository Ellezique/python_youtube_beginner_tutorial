monthConversions = {
  "Jan" : "January",
  "Feb" : "February",
  "Mar" : "March",
  4: "April",
}
print(monthConversions["Mar"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Moth", "Not a valid key"))
print(monthConversions.get(4))