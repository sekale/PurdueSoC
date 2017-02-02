/*
*		Copyright 2016 Purdue University
*		
*		Licensed under the Apache License, Version 2.0 (the "License");
*		you may not use this file except in compliance with the License.
*		You may obtain a copy of the License at
*		
*		    http://www.apache.org/licenses/LICENSE-2.0
*		
*		Unless required by applicable law or agreed to in writing, software
*		distributed under the License is distributed on an "AS IS" BASIS,
*		WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*		See the License for the specific language governing permissions and
*		limitations under the License.
*
*
*		Filename:     apb_ram_if.vh
*
*		Created by:   Siddhant Ekale
*		Email:        sekale@purdue.edu
*		Date Created: 11/28/2016
*		Description:  Interface for connecting APB bus to generic RAM interface.	
*/
`ifndef APB_RAM_IF_VH
`define APB_RAM_IF_VH

interface apb_ram_if;
   logic [31:0] PRDATA;
   logic [31:0] PWDATA;
   logic [31:0] PADDR;
   logic 	PWRITE, PENABLE, PSEL;

   modport apb_s (
     input PWDATA, PADDR, PWRITE, PENABLE, PSEL
     output PRDATA,
   );   

   modport apb_ram (
      input  PRDATA;
      output PWRITE, PWDATA, PENABLE, PWRITE, PSEL, PREADY
   );


endinterface // apb_if

`endif //  `ifndef APB_IF_VH
  
