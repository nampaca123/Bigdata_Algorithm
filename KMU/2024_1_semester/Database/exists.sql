SELECT name, address FROM Customer cs 
WHERE EXISTS(SELECT * FROM Orders od
WHERE cs.CUSTID = od.CUSTID)

-- If condition is fulfilled, it will be included to result
