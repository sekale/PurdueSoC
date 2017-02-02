// File name:   apb_plic_map.sv
// Created:     12/06/2016
// Author:      Siddhant Ekale
// Version:     1.1 

module PLIC_SlaveInterface
#(
	parameter NUMBER_OF_GATEWAYS 	= 10;
	parameter NUMBER_CLAIM_REGS 	= 10;
	parameter ADDR_OFFSET 			= 32'd0;
	parameter NUMBER_OF_TARGETS		 = 32'd1; //should be increased in case of more hart's

)
(
	input wire clk, n_rst,
	// inputs from APB Bridge
	input wire [31:0] PADDR,
	input wire [31:0] PWDATA,
	input wire PENABLE,
	input wire PWRITE,
	input wire PSEL,
	// output to APB Bridge
	output wire [31:0] PRDATA,
	output wire pslverr,


 	// input data from slave registers
	input wire [NUMBER_CLAIM_REGS-1 : 0][31:0] read_data,
	// output to slave registers
	output wire [NUMBER_CLAIM_REGS-1 : 0] w_enable,
	output wire [NUMBER_CLAIM_REGS-1 : 0] r_enable,
	output wire [31:0] w_data
);

//State machine for accessing from APB bus
typedef enum{ 
    IDLE,
    ACCESS, 
	ERROR
} APB_STATE;

APB_STATE state, next_state;

//Registers specific to the PLIC Core
//Data read
input wire [NUMBER_CLAIM_REGS-1 : 0][31:0] read_data,
//Data and registers output from the PLIC
reg[NUMBER_OF_GATEWAYS - 1:0][BUS_SIZE -1 : 0] 	gateways,
reg[NUMBER_CLAIM_REGS - 1:0][BUS_SIZE -1 : 0] claim_regs,
output wire [BUS_SIZE -1 : 0] r_data,
output wire [NUM_CLAIM_REGS - 1 : 0]  w_enable,

//Registers to help read from APB master
reg address_match;
reg [NUMBER_CLAIM_REGS-1:0] address_sel;
reg [NUMBER_CLAIM_REGS_WIDTH-1 : 0] address_index;
reg [NUMBER_CLAIM_REGS-1:0] i;
wire [11:0]slave_reg;
logic [NUMBER_CLAIM_REGS-1:0] addr_sel_preshift;

local param BYTES_PER_WORD = 4;

//check if the given address matches one in the slaves address space
always_comb
begin
  address_match = 1'b0;
  address_sel = 0;
  address_index = 0;
  addr_sel_preshift = 1;

  for(i = 0; i < NUMBER_CLAIM_REGS; i++) 
  begin 	
    if(slave_reg == ($unsigned((i * BYTES_PER_WORD)) + $unsigned(ADDR_OFFSET))) 
	begin
      address_match = 1'b1;
      address_sel = (addr_sel_preshift << i);
      address_index = i;
    end
  end
end //always_comb ends

// State Machine Register
always_ff @(posedge clk, negedge n_rst) begin
	if (n_rst == 0) begin
		state <= IDLE;
	end else begin
		state <= nextstate;
	end
end

endmodule




