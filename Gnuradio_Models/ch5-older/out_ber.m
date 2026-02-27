% Reads errors from a file and sums them

f = fopen('BER-test-data.dat', 'rb');
values = fread(f, Inf, 'float');
total_errors = sum(values(:,1))
ber = total_errors/1000
